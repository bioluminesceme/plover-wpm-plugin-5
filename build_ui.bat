@echo off
REM Build UI files from .ui to .py using pyside6-uic

echo Building WPM meter UI...
pyside6-uic --from-import plover_wpm_meter_5\wpm_meter.ui -o plover_wpm_meter_5\wpm_meter_ui.py

echo Building Strokes meter UI...
pyside6-uic --from-import plover_wpm_meter_5\strokes_meter.ui -o plover_wpm_meter_5\strokes_meter_ui.py

echo Building resources...
pyside6-rcc plover_wpm_meter_5\resources\resources.qrc -o plover_wpm_meter_5\resources_rc.py

echo Done!
