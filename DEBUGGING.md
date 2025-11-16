# Debugging Plover 5 Migration Issues

## Current Status

The plugin successfully:
- ✅ Installs via pip from GitHub
- ✅ Registers both tools (WPM Meter and Strokes Meter) in Plover's Tools menu
- ✅ Shows icons in the Tools menu

The plugin FAILS when:
- ❌ User clicks on either WPM Meter or Strokes Meter in Tools menu
- ❌ Plover crashes/exits immediately (no error logged to plover.log)
- ❌ Windows popup shows "No module named 'sqlite3'" error (but this is from plover_ninja, not our plugin)

## Environment

- Plover version: 5.1.0
- Python version: 3.13 (bundled with Plover)
- OS: Windows (MSYS_NT-10.0-26200)
- PySide6 version: 6.10.0

## What We've Tried

### 1. Fixed Import Paths ✅
- Changed `from plover_wpm_meter import` to `from plover_wpm_meter_5 import`
- Fixed `import resources_rc` to `from plover_wpm_meter_5 import resources_rc`

### 2. Removed plover from Dependencies ✅
- Removed `plover>=5.0.0` from `install_requires` in setup.cfg
- Plover is the host application and shouldn't be listed as a dependency

### 3. Fixed Build System ✅
- Changed `pyproject.toml` to only require `setuptools` and `wheel`
- Pre-built UI files using `pyside6-uic` and `pyside6-rcc`
- Removed dependency on `plover_build_utils` (which isn't on PyPI)

### 4. Renamed Package to Avoid Conflicts ✅
- Renamed from `plover_wpm_meter` to `plover_wpm_meter_5`
- Updated all references in setup.cfg, __init__.py, pyuic.json

### 5. Tried Enum Changes (REVERTED)
These changes were attempted but caused issues:
- ❌ Changed `Qt.WindowStaysOnTopHint` to `Qt.WindowType.WindowStaysOnTopHint` - REVERTED
- ❌ Changed `QLCDNumber.Flat` to `QLCDNumber.SegmentStyle.Flat` - REVERTED
- PySide6 maintains backward compatibility with PyQt5 enum syntax

### 6. Icon Troubleshooting
- Tried commenting out `ICON = ':/wpm_meter/icon.svg'` - icons disappeared from menu
- Re-enabled icons - they display correctly in the Tools menu
- Icons are NOT the cause of the crash

## Symptoms of the Crash

1. No error appears in `plover.log` when clicking Tools → WPM Meter or Tools → Strokes Meter
2. Plover shows an hourglass (loading cursor) briefly
3. Plover completely exits/crashes with no Python traceback
4. This suggests a **segmentation fault or C++ level crash** in Qt/PySide6

## Debug Information from Startup

```
2025-11-16 19:39:37,303 [MainThread] INFO: gui.qt.tool: strokes_meter (from plover.gui.qt.tool)
2025-11-16 19:39:37,430 [MainThread] INFO: gui.qt.tool: wpm_meter (from plover.gui.qt.tool)
```

Both tools register successfully during Plover startup.

## Potential Causes

### Most Likely Issues

1. **Qt Resource System Incompatibility**
   - The `resources_rc.py` file was generated with `pyside6-rcc`
   - The `.ui` files reference `<include location="resources/resources.qrc"/>`
   - The resource path `':/wpm_meter/icon.svg'` might not be properly initialized
   - **QPainter errors in old logs** suggest SVG rendering issues:
     ```
     2025-11-16 18:16:47,447 [MainThread] WARNING: Qt: QPainter::begin: Paint device returned engine == 0, type: 3
     ```

2. **QDialog/Tool Initialization Order**
   - `BaseMeter` inherits from `Tool` (which inherits from `QDialog`)
   - Must call `super().__init__(engine)` before `setupUi(self)`
   - Current code does this correctly, but there might be an issue with PySide6

3. **QLCDNumber Widget Issues**
   - The UI uses `QLCDNumber` widgets which might have compatibility issues
   - Setting properties like `segmentStyle` and `value` might fail

4. **Qt Version Mismatch**
   - Plover 5.1.0 might be using a different PySide6 version than our built UI files
   - UI files were built with PySide6 6.10.0

## What to Try Next

### Option 1: Test Without Resources
Remove the resources import and see if the window opens:
```python
# In wpm_meter_ui.py and strokes_meter_ui.py
# Comment out: from plover_wpm_meter_5 import resources_rc
```

### Option 2: Simplify the UI
Create a minimal test version with just labels, no QLCDNumber widgets.

### Option 3: Check Plover's PySide6 Version
```bash
./venv/Scripts/python -c "import PySide6; print(PySide6.__version__)"
```

Compare with Plover's bundled PySide6 version.

### Option 4: Add Exception Handling
Wrap the `__init__` in try/except to catch any Python exceptions before the C++ crash:
```python
def __init__(self, engine):
    try:
        super().__init__(engine)
        print("BaseMeter: super().__init__ succeeded")

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        print("BaseMeter: setWindowFlags succeeded")

        self.setupUi(self)
        print("BaseMeter: setupUi succeeded")

        # ... rest of init
    except Exception as e:
        print(f"ERROR in BaseMeter.__init__: {e}")
        import traceback
        traceback.print_exc()
        raise
```

### Option 5: Look at Working Plover 5 Plugins
Check how other Plover 5 plugins handle Qt Tool windows. Look in:
```
C:\Users\Corien\AppData\Local\plover\plover\plugins\win\Python313\site-packages
```

Find a working gui.qt.tool plugin and compare the code structure.

### Option 6: Test with Plover's Python
Try importing our module directly in Plover's Python interpreter:
```bash
"C:\Program Files\Open Steno Project\Plover\plover.exe" --script
>>> from plover_wpm_meter_5 import PloverWpmMeter
```

## Files Modified

- `plover_wpm_meter_5/__init__.py` - Main plugin code
- `plover_wpm_meter_5/wpm_meter_ui.py` - Generated UI file
- `plover_wpm_meter_5/strokes_meter_ui.py` - Generated UI file
- `plover_wpm_meter_5/resources_rc.py` - Generated resources file
- `setup.cfg` - Package metadata and dependencies
- `setup.py` - Simplified to just `setup()`
- `pyproject.toml` - Build system requirements
- `pyuic.json` - UI compilation configuration

## Repository

Fork: https://github.com/bioluminesceme/plover-wpm-plugin-5
Branch: main
