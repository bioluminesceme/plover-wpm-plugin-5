Plover WPM Meter
================

**Plover 5.0 Compatible Fork**
-------------------------------

This is a fork of the `original plover_wpm_meter`_ updated for **Plover 5.0** compatibility.
The migration from PyQt5 to PySide6 was performed by Claude AI (Anthropic's AI assistant).

- **Original plugin**: https://github.com/arxanas/plover_wpm_meter
- **This fork (Plover 5.0+)**: https://github.com/bioluminesceme/plover-wpm-plugin-5
- **Version**: 0.3.0+

For Plover 4.x, please use the `original plugin version 0.2.3`_.

.. _original plover_wpm_meter: https://github.com/arxanas/plover_wpm_meter
.. _original plugin version 0.2.3: https://github.com/arxanas/plover_wpm_meter/releases/tag/v0.2.3

About
-----

This is a plugin for Plover to display your typing speed as you type, in
either or both of words per minute or strokes per minute:

-  **Words per minute**: Shows the rate at which you stroked words in
   the last 10 and 60 seconds.
-  **Strokes per word**: Shows how efficiently you stroked words in
   the last 10 and 60 seconds. Lower values are more efficient, e.g. a
   value of 1 means that on average it took you one stroke to write out
   a word.

A word is defined in one of three ways:

-  **NCRA**: The `National Court Reporters Association`_ defines a
   “word” as 1.4 syllables. This is the measure used for official NCRA
   testing material.
-  **Traditional**: The traditional metric for “word” in the context of
   keyboarding is defined to be 5 characters per word, including spaces.
   This is compatible with the notion of “word” in many typing speed
   utilities.
-  **Spaces**: A word is a whitespace-separated sequence of characters.
   This metric of course doesn’t take into account the fact that some
   words are longer than others, both in length and syllables.

The meters look like this:

|The WPM meter in action| |The strokes meter in action|

License
=======

This plugin is licensed under the GPLv3.

Icon made by `Freepik`_ from `www.flaticon.com`_.

.. _National Court Reporters Association: https://www.ncra.org/
.. _Freepik: http://www.freepik.com/
.. _www.flaticon.com: http://www.flaticon.com/

.. |The WPM meter in action| image:: https://raw.githubusercontent.com/arxanas/plover_wpm_meter/master/media/wpm-meter.png
.. |The strokes meter in action| image:: https://raw.githubusercontent.com/arxanas/plover_wpm_meter/master/media/strokes-meter.png
