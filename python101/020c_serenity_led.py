import requests
import time

# SERENITY MODE: cycle through color range 0/255, where each of R/G/B is offset.

DURATION = .03 # in seconds, frequency we send updates
STEP_SIZE = 2 # with fixed DURATION, controls the speed of color shifting
RGB_ENDPOINT = 'http://10.56.4.123:8934/blink1/fadeToRGB'

red_val = 255
green_val = 127
blue_val = 0

red_increasing = True
green_increasing = True
blue_increasing = True

# infinite generator!!!
while True:
    print sum((red_val, green_val, blue_val)), red_val, green_val, blue_val

    if red_increasing:
        red_val = red_val + STEP_SIZE
    else:
        red_val = red_val - STEP_SIZE
        
    if red_val >= 255:
        red_val = 255
        red_increasing = False
    elif red_val <= 0:
        red_val = 0
        red_increasing = True
        
    if green_increasing:
        green_val = green_val + STEP_SIZE
    else:
        green_val = green_val - STEP_SIZE
        
    if green_val >= 255:
        green_val = 255
        green_increasing = False
    elif green_val <= 0:
        green_val = 0
        green_increasing = True
        
    if blue_increasing:
        blue_val = blue_val + STEP_SIZE
    else:
        blue_val = blue_val - STEP_SIZE
        
    if blue_val >= 255:
        blue_val = 255
        blue_increasing = False
    elif blue_val <= 0:
        blue_val = 0
        blue_increasing = True
        
    color_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)
    # print color_str
    
    requests.get(RGB_ENDPOINT, params={'rgb': color_str})
    
    time.sleep(DURATION)
    