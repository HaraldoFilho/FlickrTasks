# Procedures of script process-photos.py
#
# Author: Haraldo Albergaria
# Date  : Jan 01, 2018
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


###########################################
#  !!! IMPLEMENT THE PROCEDURES HERE !!!  #
###########################################


import flickrapi
import api_credentials
import json
import time

from common import isInSet
from common import hasTag
from common import getExif
from common import getFocalLength
from common import getAperture

api_key = api_credentials.api_key
api_secret = api_credentials.api_secret
user_id = api_credentials.user_id

# Flickr api access
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

fav_others_id = '72157623439971318'
galleries_id = '72157662142350881'
at10mm_id = '72157694314388675'
at250mm_id = '72157666561896128'
at1p8_id = '72157703794055595'
landscape_id = '72177720307187606'
portrait_id = '72177720307183543'
square_id = '72177720307183558'
panoramic_id = '72177720307187626'



tag = 'DNA'
summary_file = '/home/pi/flickr_tasks/auto_tasks/auto_sets/summary_sets.log'

# getExif Retries
max_retries = 10
retry_wait  = 1


#===== PROCEDURES =======================================================#

def addPhotoToSet(set_id, photo_id, photo_title):
    try:
        set_photos = flickr.photosets.getPhotos(photoset_id=set_id, user_id=user_id)
        set_title = set_photos['photoset']['title']
        flickr.photosets.addPhoto(api_key=api_key, photoset_id=set_id, photo_id=photo_id)
        print('Added photo to \'{0}\' photoset\n'.format(set_title), end='')
        summary = open(summary_file, 'a')
        summary.write('Added photo \'{0}\' to \'{1}\'\n'.format(photo_title, set_title))
        summary.close()
    except Exception as e:
        print('ERROR: Unable to add photo \'{0}\' to set \'{1}\''.format(photo_title, set_title))
        print(e)

def remPhotoFromSet(set_id, photo_id, photo_title):
    try:
        set_photos = flickr.photosets.getPhotos(photoset_id=set_id, user_id=user_id)
        set_title = set_photos['photoset']['title']
        flickr.photosets.removePhoto(api_key=api_key, photoset_id=set_id, photo_id=photo_id)
        print('Removed photo from \'{0}\' photoset\n'.format(set_title), end='')
        summary = open(summary_file, 'a')
        summary.write('Removed photo \'{0}\' from \'{1}\'\n'.format(photo_title, set_title))
        summary.close()
    except Exception as e:
        print('ERROR: Unable to remove photo \'{0}\' from set \'{1}\''.format(photo_title, set_title))
        print(e)


### !!! DO NOT DELETE OR CHANGE THE SIGNATURE OF THIS PROCEDURE !!!

def processPhoto(photo_id, photo_title, user_id):

    # Favorites of Others Set
    try:
        favorites = flickr.photos.getFavorites(photo_id=photo_id)
        photo_favs = int(favorites['photo']['total'])
        in_set = isInSet(photo_id, fav_others_id)
        print('favorites: {0}\n'.format(photo_favs), end='')
        if not in_set and photo_favs >= 1 and not hasTag(photo_id, tag):
            addPhotoToSet(fav_others_id, photo_id, photo_title)
        if in_set and (photo_favs == 0 or hasTag(photo_id, tag)):
            remPhotoFromSet(fav_others_id, photo_id, photo_title)
    except:
        print('ERROR: Unable to get information for photo \'{0}\''.format(photo_title))

    # Galleries Set
    try:
        galleries = flickr.galleries.getListForPhoto(photo_id=photo_id)
        photo_expos = int(galleries['galleries']['total'])
        in_set = isInSet(photo_id, galleries_id)
        print('galleries: {0}\n'.format(photo_expos), end='')
        if not in_set and photo_expos >= 1 and not hasTag(photo_id, tag):
            addPhotoToSet(galleries_id, photo_id, photo_title)
        if in_set and (photo_expos == 0 or hasTag(photo_id, tag)):
            remPhotoFromSet(gallleries_id, photo_id, photo_title)
    except:
        print('ERROR: Unable to get information for photo \'{0}\''.format(photo_title))

    # Lenses Exif Sets
    exif = getExif(photo_id, 0)
    try:
        focal_length = getFocalLength(exif)
        aperture = getAperture(exif)
        print('focal length: {0}\n'.format(focal_length), end='')
        print('aperture: {0}\n'.format(aperture), end='')
    except:
        print('ERROR: Unable to get information for photo \'{0}\''.format(photo_title))
        focal_length = ''
        aperture = ''
        pass

    ## @10mm
    if focal_length == '10.0 mm':
        try:
            at10mm_set = flickr.photosets.getPhotos(photoset_id=at10mm_id, user_id=user_id)
            at10mm_title = at10mm_set['photoset']['title']
            in_set = isInSet(photo_id, at10mm_id)
            if not in_set:
                addPhotoToSet(at10mm_id, photo_id, photo_title)
        except Exception as e:
            print('ERROR: Unable to add photo \'{0}\' to set \'{1}\''.format(photo_title, at10mm_title))
            print(e)

    ## @250mm
    if (focal_length == '250.0 mm' and not hasTag(photo_id, "Kenko TELEPLUS HD DGX 1.4x") and not hasTag(photo_id, "Kenko TELEPLUS HD DGX 2x")) \
        or (focal_length == '350.0 mm' and hasTag(photo_id, "Kenko TELEPLUS HD DGX 1.4x")) \
        or (focal_length == '500.0 mm' and hasTag(photo_id, "Kenko TELEPLUS HD DGX 2x")) \
        or (focal_length == '700.0 mm' and hasTag(photo_id, "Kenko TELEPLUS HD DGX 2x") and hasTag(photo_id, "Kenko TELEPLUS HD DGX 1.4x")):
        try:
            at250mm_set = flickr.photosets.getPhotos(photoset_id=at250mm_id, user_id=user_id)
            at250mm_title = at250mm_set['photoset']['title']
            in_set = isInSet(photo_id, at250mm_id)
            if not in_set:
                addPhotoToSet(at250mm_id, photo_id, photo_title)
        except Exception as e:
            print('ERROR: Unable to add photo \'{0}\' to set \'{1}\''.format(photo_title, at250mm_title))
            print(e)

    ## @f1.8
    if aperture == '1.8':
        try:
            at1p8_set = flickr.photosets.getPhotos(photoset_id=at1p8_id, user_id=user_id)
            at1p8_title = at1p8_set['photoset']['title']
            in_set = isInSet(photo_id, at1p8_id)
            if not in_set:
                addPhotoToSet(at1p8_id, photo_id, photo_title)
        except Exception as e:
            print('ERROR: Unable to add photo \'{0}\' to set \'{1}\''.format(photo_title, at1p8_title))
            print(e)


    # Format Sets
    try:
        sizes = flickr.photos.getSizes(photo_id=photo_id)['sizes']
        original_idx = len(sizes['size']) - 1
        photo_width = sizes['size'][original_idx]['width']
        photo_height = sizes['size'][original_idx]['height']
        photo_ratio = photo_width / photo_height
        print('aspect ratio: {0:.2f}\n'.format(photo_ratio), end='')
        if photo_ratio > 1 and photo_ratio < 2:
            in_set = isInSet(photo_id, landscape_id)
            if not in_set:
                addPhotoToSet(landscape_id, photo_id, photo_title)
        if photo_ratio < 1:
            in_set = isInSet(photo_id, portrait_id)
            if not in_set:
                addPhotoToSet(portrait_id, photo_id, photo_title)
        if photo_ratio == 1:
            in_set = isInSet(photo_id, square_id)
            if not in_set:
                addPhotoToSet(square_id, photo_id, photo_title)
        if photo_ratio >= 2:
            in_set = isInSet(photo_id, panoramic_id)
            if not in_set:
                addPhotoToSet(panoramic_id, photo_id, photo_title)

    except:
        print('ERROR: Unable to get information for photo \'{0}\''.format(photo_title))
