# Flickr Tasks

A collection of _python_ scripts to automate some tasks on [_Flickr™_](https://www.flickr.com/). At the moment, the following are available:

### [**_add_description/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/add_description)
   - **_add-description.py_**: Automatically add or append a description to photos on a photoset.
 
### [**_add_gear_tags/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/add_gear_tags)
   - **_add-gear-tags.py_**: Automatically add tags for the gear used (eg: camera model, lens model) according to exif data.
 
### [**_auto_add2groups/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/auto_add2groups)
   - **_add-photo-to-group.py_**: Automatically add photos to a group according to the group rules. These rules can be regarding the limit for the number of added photos (eg: 3 each day) or the actual content of the photos (eg: a given camera or lens).

### [**_auto_post2blogs/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/auto_post2blogs)
   - **_post-photo-to-blogs.py_**: Automatically post photos to all the blogs configured in the user's account.

### [**_auto_tasks/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/auto_tasks)
   - **_process-photos.py_**: Process photos in a photostream to do an action according to specified rules. e.g: Add tags to photos for views, favorites and comments counts.

### [**_best_lens/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/best_lens)
   - **_find-best-lens.py_**: Given a list of lenses, finds the best (more useful) one according to the current photos on the user's photostream or a given photoset. For each lens, the script counts how many photos were taken with a focal length covered by the lens and selects the one with the highest score. Can be used, for example, when buying a new lens, to decide from some options the one that will probably be used the most times. Or, you can use it to decide which lenses carry with you in a trip, based on a photoset with photos taken in a similar past trip (nature, city...).

### [**_check_exif/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/check_exif)
   - **_check_exif.py_**: Checks for missing exif information on photos of a photostream.  When the script is run, if there are photos with missing exif information, the photoset 'Missing Exif' will be automatically created, and they will be added to it. Also, an e-mail will be sent with the link for the photoset.

### [**_del_img_comments/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/del_img_comments)
   - **_find-image-comments.py_**: Find, in the user's photostream, comments containg images and generates the script **_delete-comments.py_** to delete them.

### [**_empty_photoset/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/empty_photoset)
   - **_empty-photoset.py_**: Empties a given photoset, leaving just 1 photo to avoid the photoset being excluded.
 
### [**_find_explored/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/find_explored)
   - **_find-photos-in-explore.py_**: Find user's photos in _Explore_ for the current day and send an e-mail with the list of photos if any is found.

### [**_focal_length_count/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/focal_length_count)
   - **_get-focal-length-count.py_**: Generates a report with the count of each focal length for all photos in an user's photostream or photoset.

### [**_generate_kml/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/generate_kml)
   - **_generate-kml.py_**: Generates two _kml_ files with the coordinates of the photos on the user's photostream, that can be imported on [_Google Earth™_](https://www.google.com/earth/) and/or [_Google My Maps™_](https://www.google.com/maps/about/mymaps/).
   - **_generate-set-kml.py_**: Generates two _kml_ files with the coordinates of the photos on a given user's photoset, that can be imported on [_Google Earth™_](https://www.google.com/earth/) and/or [_Google My Maps™_](https://www.google.com/maps/about/mymaps/).
 
### [**_group_admin/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/group_admin)
   - **_group-admin-daily-report.py_**: Reports which photos should be removed or kept in a group according to specified exif parameters. e.g.: Lens Model. Also, generates the script **_remove-photos.py_** to remove the photos that need to be removed. The report shows only the photos that were added after the last removal plus the last 100 photos before that, to guarantee that any photos added or removed during the last run will be included in the current report. Additionaly, it reports the usernames of the group's new members. Made to be run at least once a day.
   - **_group-admin-monthly-report.py_**: Same as above, but the report shows all photos since the group creation and is good to catch photos the should have been removed but for any reason were not. This can happen, for example, if photos are removed of the group by the owner after others been added, which will make some added photos do not show up in the daily report. Made to be run at least once a month.

### [**_lens_usage/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/lens_usage)
   - **_get-lens-usage.py_**: Generates a report with the usage, in number of photos and percentage of total photos in the user's photostream or a given photoset.

### [**_lenses_wide_open/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/lenses_wide_open)
   - **_find-lenses-wide-open.py_**: From a list of lenses, finds the number of photos taken with the lens diaphragm wide open, i.e. at the minimum _f/number_. Can be used also to find the number of photos taken with a _f/number_ below a given value, useful if you are thinking to replace a lens with one that has a lower minimum _f/number_ and like to know how many photos in your photostream were taken below this value to have an idea of the impact of the change.

### [**_more_stats/_**](https://github.com/HaraldoFilho/FlickrTasks/tree/master/more_stats)
   - **_show_more_stats.py_**: Calculates and show the total and medium numbers of views, favorites and comments on the user's photostream.

## Installation

The scripts were developed to run on _Linux_ systems and need _Python 3.x_ to run.

To start, open a terminal and execute the following commands:

```
git clone https://github.com/HaraldoFilho/FlickrTasks.git
cd FlickrTasks
```

The script uses *[Flickr](https://www.flickr.com/)™* API. To get and use this API follow the instructions below.

#### Flickr API key

First, install the [_flickrapi_](https://stuvel.eu/flickrapi) package by typing in a terminal:

```
% pip3 install flickrapi
```
Now, get a _Flickr_'s API key by visiting the [_Flickr_ API key request page](https://www.flickr.com/services/apps/create/apply/).

After that, create a file __api_credentials.py__ with the following code and with the obtained values:

```python
api_key = u'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api_secret = u'xxxxxxxxxxxxxxx'
user_id = 'XXXXXXXXXXXX'

```

Then, [authenticate](https://stuvel.eu/flickrapi-doc/3-auth.html#authenticating-without-local-web-server) on _Flickr_ by running:

```
% ./authenticate.py
```
A web browser will be opened to get the user approval (in a non-graphical environment, just copy and paste the authorization url in any external web browser). After approve, type in the terminal the generated code.

## Usage

- **add_description**: Inside directory 'add_description' create a link (or copy) to the file __api_credentials.py__. There are three additional files necessary to run the script:
    - **procs.py**: Open the file and read the comments to know how to customize it for your specific needs.
    - **data.py**: Include here the id of the photoset where you want to apply the description. Also, you can define if the script will overwrite or append to existent descriptions.
    - **description.txt**: Create a file containing the description you want to add or append.

- **add_gear_tags**: Inside directory 'add_gear_tags' create a link (or copy) to the file __api_credentials.py__. There are two additional files necessary to run the script:
    - **procs.py**: Open the file and read the comments to know how to customize it for your specific needs.
    - **data.py**: Include here the id of the photoset where you want to apply the tags and create dictionaries associating the exif data to the tags.

- **auto_add2groups**: Inside directory 'auto_add2groups' create a new one to your specific need (name it what you want, eg: auto_add2group_gp1) and copy the content of the directory 'files' into it. Create a link (or copy) to the file __api_credentials.py__. There are tree additional files necessary to run the script:
    - **current_id**: Include here just the id of the last photo processed by the script in the previous run. If this file is not provided or the id is invalid, the script will create a new one with the id of the last (newest) photo in the photostream. In this case, the script will run over just the photos added after it. To start the script on any photo in the photostream, set here a valid photo id. The photos will then be processed in increasing order of upload time, starting from the next photo to the id that was set here.
    - **data.py**: Include here the group data (url, limit of photos) and any other data necessary to run the script (eg: camera model, for groups of a specific camera).
    - **procs.py**: Implement here the procedures that will actually process the photos to be added to the group.

    _**TIP**: For groups that allow to add only a limited number of photos during a period (eg: 3 photos per day), create a [cron](https://opensource.com/article/17/11/how-use-cron-linux) to automatically do this._

- **auto_post2blogs**: Inside directory 'auto_post2blogs' create a link (or copy) to the file __api_credentials.py__. There are two additional files necessary to run the script:
    - **current_id**: Include here just the id of the last photo processed by the script in the previous run. If this file is not provided or the id is invalid, the script will create a new one with the id of the last (newest) photo in the photostream. In this case, the script will run over just the photos added after it. To start the script on any photo in the photostream, set here a valid photo id. The photos will then be processed in increasing order of upload time, starting from the next photo to the id that was set here.
    - **config.py**: Set here the maximum number of photos to post on each script run.

- **auto_tasks**: Inside directory 'auto_tasks' create a new one to your specific need (name it what you want, eg: auto_tags) and copy the content of the directory 'files' into it. Create a link (or copy) to the file __api_credentials.py__. There is an additional file necessary to run the script:
    - **procs.py**: Implement here the procedures that will actually process the photos.

- **best_lens**: Inside directory 'best_lens' create a link (or copy) to the file __api_credentials.py__. There are two additional file necessary to run the script:
    - **data.py**: Include here the camera maker, system and the list of lenses, following the instruction inside the file.
    - **config.py**: Include here the user id, photoset id and the privacy filter. If no photoset id is provided the script will get photos from the entire user's photostream. 

    _**IMPORTANT NOTICE:** The progress and the selected lens will be shown directly on the terminal, so the script must not be run in background. It will also be generated a report file with the score of each lens and an indication of the selected one._

- **check_exif**: Inside directory 'check_exif' create a link (or copy) to the file __api_credentials.py__. There are two additional files necessary to run the script:
    - **procs.py**: Open the file and read the comments to know how to customize it for your specific needs.
    - **mail.py**: Copy the file from 'mail_cfg' to 'check_exif' directory and edit it to add the e-mail addresses and change the e-mail subject if wanted.

- **del_img_comments**: Inside directory 'del_img_comments' create a link (or copy) to the file __api_credentials.py__. There are two additional files necessary to run the script:
    - **procs.py**: There is no need to edit this file, keep it as is.
    - **skip.py**: List to skip comments from deletion in case any text of the list is found on it.

- **empty_photoset**: Inside directory 'empty_photoset' create a link (or copy) to the file __api_credentials.py__. There is no additional files necessary to run the script and no output file will be generated. 

    _**IMPORTANT NOTICE:** The script needs user inputs, so it must not be run in background._

- **find_explored**: Inside directory 'find_explored' create a link (or copy) to the file __api_credentials.py__. There are two additional file necessary to run the script:
    - **procs.py**: Open the file and edit the variable _set_id_ with the id of the photoset to where the explored photos will be added.
    - **mail.py**: Copy the file from 'mail_cfg' to 'find_explored' directory and edit it to add the e-mail addresses and change the e-mail subject if wanted.

    _**TIP**: Create a [cron](https://opensource.com/article/17/11/how-use-cron-linux) to automatically check for photos in Explore and configure it to run at least once a day._

- **focal_length_count**: Inside directory 'focal_length_count' create a link (or copy) to the file __api_credentials.py__. There is one additional file necessary to run the script:
    - **config.py**: Include here the user id, photoset id and the privacy filter. If no photoset id is provided the script will get photos from the entire user's photostream. 

    _**IMPORTANT NOTICE:** The progress and the selected lens will be shown directly on the terminal, so the script must not be run in background. It will also be generated a report file with the count of each focal length._

- **generate_kml**: Inside directory 'generate_kml' create a link (or copy) to the file __api_credentials.py__. There are four additional files necessary to run the scripts:
    - **procs.py**: There is no need to edit this file, keep it as is.
    - **header.earth.kml** and **header.mymaps.kml**: These files contain the initial code for the generated _kml_ files. **Do not delete any of them, otherwise the generated file will be useless**. The generated files will be **my_flickr_photos.earth.kml** and **my_flickr_photos.mymaps.kml**.
    - **config.py**: If there are photos that must not be included on the map, add the tag in the variable _dont_map_tag_ to it. When running _generate-set-kml.py_, edit the variable _photoset_id_ with the id of the photoset containing the photos that will be included on the map.

- **group_admin**: Inside directory 'group_admin' create a new one to your specific need (name it what you want, eg: group_name) and copy the content of the directory 'files' into it. Create a link (or copy) to the file __api_credentials.py__. There are two additional files necessary to run the script:
    - **group_data.py**: Include here the id, alias and url of the group.
    - **procs.py**: Implement here the procedures that will actually process the photos to generate the reports.

- **lens_usage**: Inside directory 'lens_usage' create a link (or copy) to the file __api_credentials.py__. There is one additional file necessary to run the script:
    - **config.py**: Include here the camera maker and/or the photoset id, following the instruction inside the file.

    _**IMPORTANT NOTICE:** The progress will be shown directly on the terminal, so the script must not be run in background. It will also be generated a report file with the usage data for each lens._

- **lenses_wide_open**: Inside directory 'lenses_wide_open' create a link (or copy) to the file __api_credentials.py__. There is one additional file necessary to run the script:
    - **data.py**: Include here the camera maker, system and the list of lenses, following the instruction inside the file. To find the number of photos taken with a _f/number_ below a given value, change the 'mode' variable value from 'wide_open' to 'max_open'. 

    _**IMPORTANT NOTICE:** The progress will be shown directly on the terminal, so it is recommended to not run the script in background. It will be generated a report file with the number of photos taken with the diaphragm wide open for each lens._

- **more_stats**: Inside directory 'more_stats' create a link (or copy) to the file __api_credentials.py__. There is no additional files necessary to run the script and no output file will be generated.

    _**IMPORTANT NOTICE:** The progress and the results will be shown directly on the terminal, so the script must not be run in background._

### IMPORTANT WARNING! Please, read before use these scripts:
**To use these scripts it is necessary a basic knowledge of computer programming in _Python_.** They were written for my specific needs of automating tasks on [my Flickr account](https://www.flickr.com/photos/hpfilho/) and I don't know if they will be useful for anyone else. But, if you want to use them, when using the **group_admin** scripts, always review carefully the results of the generated **_remove-photos.py_** and only after that run it. If you don't do this, there is a chance of removing "good" files (or even end up with an empty group pool!), in case there is any changes in the way _Flickr_ returns the EXIF data or an error in your procedures implementation.  **Please, use these scripts with care and at your own risk.**

