# metal_concerts

A Python script to find interesting metal concerts near me.

> [!WARNING]
> This script is currently not working due to limited access to Encyclopaedia Metallum's pages.

The script works by pulling down a list of bands playing near from an [online calendar](http://www.wrekage.org/events.php).
The script then looks up each band on a [metal band database](http://www.metal-archives.com/) and returns the bands that match my particular genre choices.

# Dependencies

* Python 3

# How to use

1. Download the `metal_concerts.py` script.
2. Navigate to the directory where it was downloaded.
3. Enter `python metal_concerts.py` to run the script.
4. Optionally, add in your preferred metal subgenres for more specific results (e.g. `python metal_concerts.py doom metal`).
