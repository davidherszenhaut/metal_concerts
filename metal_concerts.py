#!/usr/bin/env python3

"""Script to look up metal concerts in Atlanta"""



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
#



def get_band_list():

    # get calendar HTML as text
    request = urllib.request.Request("http://www.wrekage.org/events.php")
    response = urllib.request.urlopen(request)
    page_bytes = response.read()
    page_text = page_bytes.decode()

    # get list of performing bands in <strong> tags
    band_list = re.findall(r'<strong>(.+?)</strong>', page_text.replace("\n", ""))

    # remove last 18 bands because they are not part of the calendar
    band_list = band_list[:-18]

    # split any bands separated by commas
    band_list = [band.split(",") for band in band_list]

    # flatten any nested lists created
    band_list = [x for y in band_list for x in y]

    band_list = [band.strip() for band in band_list]

    return band_list

def get_band_genres(band_list):

    # create list with underscores for url creation
    band_list_underscore = [band.replace(" ", "_").strip() for band in band_list]

    # make an empty dictionary for band(str): genre(str)
    band_dict = {}

    # populate dictionary with metal-archives.com information
    for i in range(len(band_list)):

        try:

            # get band page HTML as text
            current_request = urllib.request.Request("http://www.metal-archives.com/bands/" + band_list_underscore[i])
            current_response = urllib.request.urlopen(current_request)
            current_bytes = current_response.read()
            current_text = current_bytes.decode()

            # find genre in <dd> tags
            dd_tags = re.findall(r'<dd>(.+?)</dd>', current_text.replace("\n", ""))
            current_genre = dd_tags[3]

            # add band and genre to band_dict
            band_dict[band_list[i]] = current_genre

            print("The band " + band_list[i] + " was found. Its genre is " + band_dict[band_list[i]] + ".")

        except:

            # band was not found
            print("The band " + band_list[i] + " was not found.")

    return band_dict



def bands_with_style(band_dict, genre_list):

    for band, genre in band_dict.items():
        for style in genre_list:
            if style in genre.lower():
                print(band + " plays with the style: " + style + ".")

if __name__ == "__main__":

    print("Enter a space-separated list of the genres you like:")
    genre_list = input("> ")
    genre_list = genre_list.split(" ")
    genre_list = [genre.lower() for genre in genre_list]

    band_list = get_band_list()
    band_dict = get_band_genres(band_list)
    bands_with_style(band_dict, genre_list)