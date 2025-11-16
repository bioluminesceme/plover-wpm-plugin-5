import time

from PySide6.QtCore import Qt, QTimer

from plover.gui_qt.tool import Tool
from plover.formatting import OutputHelper
from textstat.textstat import textstat

from plover_wpm_meter_5.strokes_meter_ui import Ui_StrokesMeter
from plover_wpm_meter_5.wpm_meter_ui import Ui_WpmMeter


class CaptureOutput(object):

    def __init__(self, chars):
        self.chars = chars

    def send_backspaces(self, n):
        del self.chars[-n:]

    def send_string(self, s):
        self.chars += _timestamp_items(s)

    def send_key_combination(self, c):
        pass

    def send_engine_command(self, c):
        pass


class BaseMeter(Tool):
    def __init__(self, engine):
        try:
            print("[DEBUG] BaseMeter.__init__ starting")
            print(f"[DEBUG] Engine type: {type(engine)}")

            print("[DEBUG] Calling super().__init__(engine)")
            super().__init__(engine)
            print("[DEBUG] super().__init__ completed successfully")

            print("[DEBUG] Setting window flags")
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            print("[DEBUG] Window flags set successfully")

            print("[DEBUG] Calling setupUi(self)")
            self.setupUi(self)
            print("[DEBUG] setupUi completed successfully")

            print("[DEBUG] Connecting is_pinned_checkbox")
            self.is_pinned_checkbox.stateChanged.connect(self.set_is_pinned)
            print("[DEBUG] is_pinned_checkbox connected")

            print("[DEBUG] Creating QTimer")
            self._timer = QTimer()
            self._timer.setInterval(1000)
            self._timer.setTimerType(Qt.PreciseTimer)
            self._timer.timeout.connect(self.on_timer)
            self._timer.start()
            print("[DEBUG] QTimer started")

            print("[DEBUG] Calling restore_state()")
            self.restore_state()
            print("[DEBUG] restore_state completed")

            print("[DEBUG] Connecting finished signal")
            self.finished.connect(self.save_state)
            print("[DEBUG] finished signal connected")

            print("[DEBUG] Initializing chars list")
            self.chars = []
            print("[DEBUG] Connecting translated signal")
            engine.signal_connect("translated", self.on_translation)
            print("[DEBUG] BaseMeter.__init__ completed successfully!")

        except Exception as e:
            print(f"[ERROR] Exception in BaseMeter.__init__: {e}")
            import traceback
            traceback.print_exc()
            raise

    def on_translation(self, old, new):
        output = CaptureOutput(self.chars)
        output_helper = OutputHelper(output, False, False)
        output_helper.render(None, old, new)

    def on_timer(self):
        raise NotImplementedError()

    def _save_state(self, settings):
        settings.setValue("is_pinned", self.is_pinned_checkbox.isChecked())

    def _restore_state(self, settings):
        is_pinned = settings.value("is_pinned", True, bool)
        self.is_pinned_checkbox.setChecked(is_pinned)

    def set_is_pinned(self):
        is_pinned = self.is_pinned_checkbox.isChecked()
        if is_pinned:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()


class PloverWpmMeter(BaseMeter, Ui_WpmMeter):

    TITLE = "WPM Meter"
    ROLE = "wpm_meter"
    # ICON = ':/wpm_meter/icon.svg'  # COMMENTED OUT FOR TESTING

    _TIMEOUTS = {
        "wpm1": 10,
        "wpm2": 60,
    }

    def __init__(self, engine):
        print("[DEBUG] PloverWpmMeter.__init__ starting")
        super().__init__(engine)
        print("[DEBUG] PloverWpmMeter: super().__init__ completed")
        self.strokes = []
        self.wpm_method.addItem("NCRA (by syllables)", "ncra")
        self.wpm_method.addItem("Traditional (by characters)", "traditional")
        self.wpm_method.addItem("Spaces (by whitespace)", "spaces")
        print("[DEBUG] PloverWpmMeter.__init__ completed")

    def on_timer(self):
        max_timeout = max(self._TIMEOUTS.values())
        self.chars = _filter_old_items(self.chars, max_timeout)
        for name, timeout in self._TIMEOUTS.items():
            chars = _filter_old_items(self.chars, timeout)
            wpm = _wpm_of_chars(chars, method=self.wpm_method.currentData())
            getattr(self, name).display(str(wpm))


class PloverStrokesMeter(BaseMeter, Ui_StrokesMeter):

    TITLE = "Strokes Meter"
    ROLE = "strokes_meter"
    # ICON = ':/wpm_meter/icon.svg'  # COMMENTED OUT FOR TESTING

    _TIMEOUTS = {
        "strokes1": 10,
        "strokes2": 60,
    }

    def __init__(self, engine):
        print("[DEBUG] PloverStrokesMeter.__init__ starting")
        super().__init__(engine)
        print("[DEBUG] PloverStrokesMeter: super().__init__ completed")
        self.strokes_method.addItem("NCRA (by syllables)", "ncra")
        self.strokes_method.addItem("Traditional (by characters)",
                                    "traditional")
        self.strokes_method.addItem("Spaces (by whitespace)", "spaces")
        self.actions = []

        # By default, the QLCDNumbers will just display "0", without a decimal
        # point, on initial render. Render them ourselves so that we don't
        # switch from "0" to "0.00" after a second.
        print("[DEBUG] PloverStrokesMeter: calling on_timer()")
        self.on_timer()
        print("[DEBUG] PloverStrokesMeter.__init__ completed")

    def on_translation(self, old, new):
        super().on_translation(old, new)
        if len(old) > 0:
            self.actions = self.actions[:-len(old)]
        self.actions += _timestamp_items(new)

    def on_timer(self):
        max_timeout = max(self._TIMEOUTS.values())
        self.chars = _filter_old_items(self.chars, max_timeout)
        self.actions = _filter_old_items(self.actions, max_timeout)
        for name, timeout in self._TIMEOUTS.items():
            chars = _filter_old_items(self.chars, timeout)
            num_strokes = len(_filter_old_items(self.actions, timeout))
            strokes_per_word = _spw_of_chars(
                num_strokes,
                chars,
                method=self.strokes_method.currentData()
            )
            getattr(self, name).display("{:0.2f}".format(strokes_per_word))


def _timestamp_items(items):
    current_time = time.time()
    return [(i, current_time) for i in items]


def _filter_old_items(items, timeout):
    current_time = time.time()
    return [(i, t) for i, t in items
            if (current_time - t) <= timeout]


def _words_in_chars(chars, method):
    text = "".join(c for c, _ in chars)
    if method == "ncra":
        # The NCRA defines a "word" to be 1.4 syllables, which is the average
        # number of syllables per English word.
        syllables_per_word = 1.4
        # For some reason, textstat returns syllable counts such as a
        # one-syllable word like "the" being 0.9 syllables.
        syllables_in_text = textstat.syllable_count(text) / 0.9
        return syllables_in_text * (1 / syllables_per_word)
    elif method == "traditional":
        # Formal definition; see https://en.wikipedia.org/wiki/Words_per_minute
        return len(text) / 5
    elif method == "spaces":
        return len([i for i in text.split() if i])
    else:
        assert False, "bad wpm method: " + method


def _time_interval_of_chars(chars):
    start_time = min(t for _, t in chars)
    current_time = time.time()
    time_interval = current_time - start_time
    time_interval = max(1, time_interval)
    return time_interval


def _wpm_of_chars(chars, method):
    num_words = _words_in_chars(chars, method)
    if not num_words:
        return 0

    time_interval = _time_interval_of_chars(chars)
    num_minutes = time_interval / 60
    num_words_per_minute = num_words / num_minutes
    return int(round(num_words_per_minute))


def _spw_of_chars(num_strokes, chars, method):
    num_words = _words_in_chars(chars, method)
    if not num_words:
        return 0

    return num_strokes / num_words
