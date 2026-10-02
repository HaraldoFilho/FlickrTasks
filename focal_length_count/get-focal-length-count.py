#!/usr/bin/python3

# This script counts the number of photos taken for each focal length
#
# Author: Haraldo Albergaria
# Date  : Oct 1, 2026
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import flickrapi
import api_credentials
import config
import json
import time
import os

from common import getExif
from common import getCameraMaker
from common import getCameraModel
from common import getFocalLength

# Credentials
api_key = api_credentials.api_key
api_secret = api_credentials.api_secret
user_id = api_credentials.user_id

# Flickr api access
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# getExif retries
max_retries = 10
retry_wait  = 1

# report file name
report_file_name = "focal_length_count_report.txt"

# photoset id
photoset_id = ''

#===== Procedures ===========================================================#

def genReport(data, file_name):
    report_file = open(file_name, "w")
    report_file.write("+-----------------------+\n")
    report_file.write("| Focal Length | Photos |\n")
    report_file.write("+-----------------------+\n")
    for i in range(len(data)):
        focal_length = data[i][0]
        photos = data[i][1]
        report_file.write("| {0:9} mm | {1:>6} |\n".format(focal_length, photos))
    report_file.write("+-----------------------+\n")
    report_file.close()

def sort_criteria(e):
    return e[1]


#===== MAIN CODE ==============================================================#

if config.photoset_id != '':
    photos = flickr.photosets.getPhotos(api_key=api_key, user_id=user_id, photoset_id=config.photoset_id, privacy_filter=config.photo_privacy, content_types=0)
    npages = int(photos['photoset']['pages'])
    total_photos = int(photos['photoset']['total'])
    title = photos['photoset']['title']
    print("Getting focal length stats for album: {}".format(title))
    print("Please, wait...")
else:
    photos = flickr.people.getPhotos(user_id=user_id, content_types=0)
    npages = int(photos['photos']['pages'])
    total_photos = int(photos['photos']['total'])
    print("Getting focal length stats... Please, wait.")


photo = 0
focal_lengths = []
found = 0

for pg in range(1, npages+1):
    if config.photoset_id != '':
        page = flickr.photosets.getPhotos(api_key=api_key, user_id=user_id, photoset_id=config.photoset_id, privacy_filter=config.photo_privacy, content_types=0)
        photos = page['photoset']
    else:
        page = flickr.people.getPhotos(user_id=user_id, content_types=0, page=pg)
        photos = page['photos']

    ppage = len(photos['photo'])

    for ph in range(0, ppage):
        photo = photo + 1
        photo_id = photos['photo'][ph]['id']

        try:
            exif = getExif(photo_id, 0, False)
            focal_length = getFocalLength(exif)
            if focal_length == '':
                focal_length = 0
            else:
                focal_length = float(focal_length.replace(' mm', ''))
        except:
            break

        found = 0
        if (len(focal_lengths) == 0):
            focal_lengths.append([focal_length, 1])
        for i in range(len(focal_lengths)):
            if focal_length == focal_lengths[i][0]:
                focal_lengths[i][1] += 1
                found = 1
                break
        if not (found):
            focal_lengths.append([focal_length, 1])

        print("Processed photo {0}/{1}".format(photo, total_photos), end='\r')

focal_lengths.sort(reverse=True, key=sort_criteria)

genReport(focal_lengths, report_file_name)
os.system("more {}".format(report_file_name))


