# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Plover plugin that displays real-time typing speed metrics in two windows:
- **WPM Meter**: Shows words per minute for the last 10 and 60 seconds
- **Strokes Meter**: Shows strokes per word efficiency for the last 10 and 60 seconds

Both meters support three word-counting methods:
- **NCRA**: Counts by syllables (1.4 syllables = 1 word)
- **Traditional**: 5 characters = 1 word (standard typing test metric)
- **Spaces**: Whitespace-separated sequences

**Version 0.3.0+**: Updated for Plover 5.0 with PySide6 support (migrated from PyQt5).

## Development Commands

### Building
```bash
python setup.py build_ui    # Build UI files from .ui resources
python setup.py build_py    # Build Python files (depends on build_ui)
python setup.py develop     # Install in development mode (depends on build_py)
```

The build process uses `plover_build_utils` to compile PySide6 UI files (.ui) into Python modules. UI compilation is configured in `pyuic.json` using `pyside6-uic` with the `--from-import` flag.

### Testing
```bash
pytest                      # Run all tests
pytest test/test_plover_wpm_meter.py  # Run specific test file
```

## Architecture

### Plugin Registration
The plugin registers two Qt tools via entry points in `setup.cfg`:
- `plover.gui.qt.tool` → `wpm_meter` and `strokes_meter`

### Core Components

**BaseMeter** (`plover_wpm_meter/__init__.py`):
- Abstract base class for both meter types
- Handles window pinning (stay-on-top functionality)
- Connects to Plover's `translated` signal to capture strokes
- Uses `CaptureOutput` to intercept and timestamp output characters via `OutputHelper`
- Runs a 1-second `QTimer` to update displays

**PloverWpmMeter**:
- Inherits from `BaseMeter` and `Ui_WpmMeter` (generated from `wpm_meter.ui`)
- Displays WPM for 10s and 60s windows
- Uses `_wpm_of_chars()` to calculate WPM based on selected method

**PloverStrokesMeter**:
- Inherits from `BaseMeter` and `Ui_StrokesMeter` (generated from `strokes_meter.ui`)
- Tracks both characters and translation actions (strokes)
- Displays strokes-per-word ratio as a decimal (e.g., "1.25")
- Handles undo by removing items from the `actions` list

### Key Data Structures
- `chars`: List of `(character, timestamp)` tuples representing output
- `actions`: List of `(translation, timestamp)` tuples representing strokes (strokes meter only)
- Items are filtered by time window using `_filter_old_items()`

### UI Files
- `wpm_meter.ui` and `strokes_meter.ui` are Qt Designer files
- Compiled to `wpm_meter_ui.py` and `strokes_meter_ui.py` by build process
- Icon loaded from `resources/icon.svg` via Qt resource system

### Dependencies
- `plover>=5.0.0`: Host application and API (requires Plover 5 for PySide6 support)
- `textstat==0.3.1`: Syllable counting for NCRA method (pinned due to encoding bug)
- PySide6: UI framework (installed as Plover 5 dependency)

## Testing Notes
Tests use `mock.patch("time.time")` to control timestamps for deterministic results. The core calculation functions (`_wpm_of_chars`, `_filter_old_items`, etc.) are tested independently from the Qt UI.

## CRITICAL: PySide6 on Windows Issues

### ⚠️ DO NOT USE EMOJI IN UI TEXT
**NEVER use emoji characters in PySide6 widgets on Windows** - they cause immediate crashes (segfault at C++ level).

**Problem**: The original PyQt5 version used 📌 emoji (`\ud83d\udccc`) for the pin checkbox text. When migrated to PySide6, this caused Plover to crash immediately when opening the tool windows.

**Solution**: Replace all emoji with plain text. For example:
- ❌ `self.is_pinned_checkbox.setText("📌")`
- ✅ `self.is_pinned_checkbox.setText("Pin")`

**Root Cause**: The crash occurred in `retranslateUi()` when calling `setText()` with emoji on QCheckBox widgets. This appears to be a PySide6/Qt encoding or font rendering issue specific to Windows.

**Debugging Notes**: The crash produced no Python traceback - only a C++ segfault. Debug output via `print()` statements (visible in `plover_console.exe --log-level debug`) was essential to pinpointing the exact line.
