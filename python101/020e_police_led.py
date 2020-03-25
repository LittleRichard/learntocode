import requests
import time

# written by Jess Armstrong for coding101 round 1

# police MODE: flash random colors

DURATION = .1 # in seconds
SHORT_DUR = .05
RGB_ENDPOINT = 'http://10.56.4.123:8934/blink1/fadeToRGB'

red_val = 255
blue_val = 255
green_val = 255
null_val = 0

red_str = '#%.2x%.2x%.2x' % (red_val, null_val, null_val)
blue_str = '#%.2x%.2x%.2x' % (null_val, null_val, blue_val)
white_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)

while True:

    i = 0
    while i < 2:
        requests.get(RGB_ENDPOINT, params={'rgb': red_str})
        time.sleep(DURATION)
        print('red')

        requests.get(RGB_ENDPOINT, params={'rgb': blue_str})
        time.sleep(DURATION)
        print('blue')

        i += 1

    requests.get(RGB_ENDPOINT, params={'rgb': white_str})
    time.sleep(SHORT_DUR)
    print('white')
