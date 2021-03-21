import requests

# some helpful links:
# https://requests.readthedocs.io/en/master/user/quickstart/
# https://requests.readthedocs.io/en/master/api/#requests.request
# https://requests.readthedocs.io/en/master/api/#requests.Response
# https://dog.ceo/dog-api/documentation/breed

# TODO: steal code from class to get started, then:
# access the Dog API to get the breeds list
# choose a random breed
# access the images the Dog API has for that breed
# choose a random image URL
# download the image data and store it in a file
# # Note: images are binary data, so google your way
# # through routing the 'content' of the response
# # into a file and trust that an image viewing program
# # will know what to do

# Finally: (not in python) admire the cute pup photo
# BONUS: download ALL OF THE CUTE PUP PHOTOS
# Hint: a function might help us organize this code

import time
def download_random_image(breed, sub_breed=None):
    # if you do this, be kind to the free dog API and
    # rate-limit your script; here's how you make the
    # script take a break
    # 250 milliseconds is a long time.
    time.sleep(.25)

# TODO: do either the bonus from the dog API or this
# choose an API that interests you from:
# https://github.com/public-apis/public-apis
#
# figure out how to exchange data with the API. if 
# your API requires authentication, figuring that out
# and making any successful request is plenty! otherwise,
# make a script that performs a few actions.
# be prepared to demo your results in class!!!
# 
# WARNING: Don't pick an 'OAuth' authenticated API, too complex.

print('You probably want to do this in another script')