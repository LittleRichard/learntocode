import requests
# the requests library lets you make HTTP calls (just like a web browser)
# to a specified URL.  The URL is the server's address, and depending
# on which specific endpoint you access you can retrieve HTML files,
# encoded data (usually in the form of a dictionary), or binary data
# like audio/video/pictures.

# the reason i like programming is that it applies to many topics,
# and you end up learning about some pretty random stuff along the way
# to completing any given project.
# In this case, we'll learn about colors!

# Simple mode: set a color
# individual color values are 0->255 (AKA a byte, requires 8 bits because 256 = 2^8)
# an RGB color is composed of 3 values, each representing the intensity of one primary color
# http://www.rapidtables.com/web/color/RGB_Color.htm

# read the docs: the server wants a 'hexadecimal' value
# BITS AND BYTES, sorry!
# binary (base 2) uses 1s and 0s
# base 10 uses 0-9
# hexadecimal is base 16, uses 0-9 and a-f, where a=10, b=11... f=15
# a byte is represented by two hex characters
# %s -> strings, %f -> floats, %d -> integers, %x -> hexadecimal values

red_val = 5
print('integer: %d, binary: %s, hex: %x' % (red_val, bin(red_val), red_val))
green_val = 60
print('integer: %d, binary: %s, hex: %x' % (green_val, bin(green_val), green_val))
blue_val = 103
print('integer: %d, binary: %s, hex: %x' % (blue_val, bin(blue_val), blue_val))
# this formats a string like '#3579ac'
## The '#' is required by the server.
# where 35 is the red val (as hex), 79 is the green val (as hex), and ac is the blue val (as hex)
# the %.2x says to use:
## a hex value with 2 characters
## any value only needing 1 character should pad with zeroes
color_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)
print(color_str)

RGB_ENDPOINT = 'http://10.56.4.123:8934/blink1/fadeToRGB'
my_payload = {'rgb': color_str}
requests.get(RGB_ENDPOINT, params=my_payload)