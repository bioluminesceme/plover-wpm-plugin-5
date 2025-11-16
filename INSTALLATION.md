# Installation Instructions

## For Plover 5.0+

### From PyPI (Recommended)
Once published, install via Plover's Plugin Manager:

1. Open Plover
2. Go to Tools → Plugins Manager
3. Search for "plover-wpm-meter"
4. Click Install
5. Restart Plover

### From Local Repository

#### Regular Installation

**Using pip (Recommended):**
```bash
cd F:\Steno\plover_wpm_meter
pip install .
```

**Using Plover's Plugin Manager (Requires GitHub URL):**
1. Fork this repository to your GitHub account
2. Open Plover
3. Go to Tools → Plugins Manager
4. Click "Install Plugin" (the + button)
5. Enter your forked GitHub URL: `https://github.com/YOUR-USERNAME/plover_wpm_meter`
   - Plover automatically adds the `git+` prefix
6. Restart Plover

**Note:** Plover's Plugin Manager expects a Git repository URL and cannot install from local directories. For local installation, use pip directly (see below).

#### Development Installation (Editable)
For development work where changes take effect without reinstalling:
```bash
cd plover_wpm_meter
pip install -r requirements-dev.txt
pip install -e .
```

Or using the legacy method:
```bash
cd plover_wpm_meter
pip install -r requirements-dev.txt
python setup.py develop
```

## For Plover 4.x (Legacy)

**Note:** Version 0.3.0+ requires Plover 5.0 or later. For Plover 4.x, install version 0.2.3:

```bash
pip install plover-wpm-meter==0.2.3
```

Or use the Plugin Manager to install the older version.

## Usage

After installation and restarting Plover:

1. Go to **Tools → WPM Meter** to display the words-per-minute meter
2. Go to **Tools → Strokes Meter** to display the strokes-per-word efficiency meter

Both meters can be used simultaneously and offer three word-counting methods (NCRA, Traditional, or Spaces).
