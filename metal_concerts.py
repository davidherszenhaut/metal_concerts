#!/usr/bin/env python3

"""Script to look at metal concerts in Atlanta and produce a static website representing the ones worth attending."""

import urllib.request
import re

__author__ =     "David Herszenhaut"
__copyright__ =  "Copyright 2017"
__credits__ =    []
__license__ =    "GNU GPL v3"
__version__ =    "1.0.0"
__maintainer__ = "David Herszenhaut"
__email__ =      "david.herszenhaut@gmail.com"
__status__ =     "Development"

# TODO
# try to make some kind of index.html
# use python -m http.server and webbrowser to open index.html

# get .html as text
request = urllib.request.Request("http://www.wrekage.org/events.php")
response = urllib.request.urlopen(request)
page_bytes = response.read()
page_text = page_bytes.decode()

# get list of bands because they are all in <strong> tags
band_list = re.findall(r'<strong>(.+?)</strong>', page_text.replace("\n", ""))

# remove the last 18 bands because they are not really there
band_list = band_list[:-18]

# replace spaces with underscores for url purposes
band_list_underscore = [band.replace(" ", "_").strip() for band in band_list]

# make an empty dictionary for band (str): genre (str)
band_dict = {}

# loop over band list to fill dictionary
for i in range(len(band_list)):

    try:

        # get .html as text
        current_request = urllib.request.Request("http://www.metal-archives.com/bands/" + band_list_underscore[i])
        current_response = urllib.request.urlopen(current_request)
        current_bytes = current_response.read()
        current_text = current_bytes.decode()

        # find genre inside <dd> tags
        dd_tags = re.findall(r'<dd>(.+?)</dd>', current_text.replace("\n", ""))
        current_genre = dd_tags[3]

        # add to dictionary
        band_dict[band_list[i]] = current_genre
    
        # print("This band is kvlt (" + current_band + ").")
        print("The band " + band_list[i] + " was found. Its genre is " + band_dict[band_list[i]] + ".")

    except:

        # print("This band is not kvlt (" + current_band + ").")
        print("The band " + band_list[i] + " was not found.")

for band, genre in band_dict.items():
    if "doom" in genre.lower():
        print(band + " plays doom metal (" + genre + ").")
    elif "melodic" in genre.lower():
        print(band + " plays melodic metal (" + genre + ").")
    elif "black" in genre.lower():
        print(band + " plays black metal (" + genre + ").")
    elif "heavy" in genre.lower():
        print(band + " plays heavy metal (" + genre + ").")
    elif "power" in genre.lower():
        print(band + " plays power metal (" + genre + ").")
