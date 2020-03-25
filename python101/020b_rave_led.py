import requests
import random
import time

# RAVE MODE: flash random colors

DURATION = .05 # in seconds
RGB_ENDPOINT = 'http://10.56.4.123:8934/blink1/fadeToRGB'

while True:
    red_val = random.randint(0,255)
    green_val = random.randint(0,255)
    blue_val = random.randint(0,255)
    
    print 'R%s, G%s, B%s' % (red_val, green_val, blue_val)
    
    color_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)
    
    if (red_val + green_val + blue_val) >= 127:
        requests.get(RGB_ENDPOINT, params={'rgb': color_str})
        time.sleep(DURATION) # tells the computer to do nothing for a fixed duration.
    else: 
        # skip because the random value is too dim
        print('skipping, too dim')