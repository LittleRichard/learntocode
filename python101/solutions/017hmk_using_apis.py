import random
import requests
import time

# some helpful links:
# https://requests.readthedocs.io/en/master/user/quickstart/
# https://requests.readthedocs.io/en/master/api/#requests.request
# https://requests.readthedocs.io/en/master/api/#requests.Response
# https://dog.ceo/dog-api/documentation/breed

# TODO: steal code from class to get started, then:
DOG_API_BASE_URL = 'https://dog.ceo/api/'
ALL_BREEDS_PATH = DOG_API_BASE_URL + 'breeds/list/all'

# access the Dog API to get the breeds list
breeds_resp = requests.get(ALL_BREEDS_PATH)
breeds_json = breeds_resp.json()
breeds = breeds_json['message']

# choose a random breed
rand_breed = random.choice(list(breeds.keys()))

# access the images the Dog API has for that breed
images_url = DOG_API_BASE_URL + f'breed/{rand_breed}/images'
img_resp = requests.get(images_url)
img_json = img_resp.json()

# choose a random image URL
rand_image_url = random.choice(img_json['message'])

# download the image data and store it in a file
print(f'downloading pup image {rand_image_url}')
img_resp = requests.get(rand_image_url)
output_file_path = f'data/random_{rand_breed}.jpg'
with open(output_file_path, 'wb') as fh:
    fh.write(img_resp.content)

# (not in python, just clicking) admire the cute pup photo
print(f'check that pup out at {output_file_path}')

# BONUS: download one photo for EACH breed
# BONUS BONUS: handle the breed subtypes
# 
# Warning: if you do this, be kind to the free dog API
# and rate-limit your script; here's how you make the
# script take a break

# Hint: a function might help us organize this code
def download_random_image(breed, sub_breed=None):

    if sub_breed:
        breed_path = f'{breed}/{sub_breed}'
    else:
        breed_path = breed

    images_url = (
        DOG_API_BASE_URL +
        f'breed/{breed_path}/images')

    img_resp = requests.get(images_url)
    img_json = img_resp.json()

    # choose a random image URL
    rand_image_url = random.choice(img_json['message'])

    # download the image data and store it in a file
    print(f'downloading pup image {rand_image_url}')
    img_resp = requests.get(rand_image_url)

    # it's ok if sub_breed is None, but will appear
    # the file name that way
    output_file_path = f'data/random_{breed}_{sub_breed}.jpg'
    with open(output_file_path, 'wb') as fh:
        fh.write(img_resp.content)

    time.sleep(.25)  # be kind to the dog API

for breed, subtypes in breeds.items():

    # if there are sub breeds
    if len(subtypes) > 0:
        for sub_breed in subtypes:
            download_random_image(breed, 
                                  sub_breed=sub_breed)
    else:
        download_random_image(breed)

# TODO:
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
