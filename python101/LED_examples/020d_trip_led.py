import requests
import random
import time

# TRIP MODE: smoothly cycle between random colors

DURATION = .1 # in seconds, frequency we send updates
STEP_SIZE = 5 # with fixed DURATION, controls the speed of color shifting
RGB_ENDPOINT = 'http://10.56.4.123:8934/blink1/fadeToRGB'

red_val = 255
green_val = 255
blue_val = 255

target_red_val = red_val
target_green_val = green_val
target_blue_val = blue_val

# infinite!!!
while True:
    # print sum((red_val, green_val, blue_val)), red_val, green_val, blue_val

    if (abs(red_val - target_red_val) < STEP_SIZE and 
        abs(green_val - target_green_val) < STEP_SIZE and 
        abs(blue_val - target_blue_val) < STEP_SIZE):
        # ideally we'll pick from the full range
        target_red_val = random.randint(0,255)
        target_green_val = random.randint(0,255)
        target_blue_val = random.randint(0,255)

        # scale so that one value is always 255 to avoid dim targets
        max_val = float(max(target_red_val, target_green_val, target_blue_val))
        target_red_val = int((target_red_val / max_val) * 255)
        target_green_val = int((target_green_val / max_val) * 255)
        target_blue_val = int((target_blue_val / max_val) * 255)

        print 'New target R(%s) G(%s) B(%s)' % (target_red_val, target_green_val, target_blue_val)

    if abs(red_val - target_red_val) >= STEP_SIZE:
        if target_red_val > red_val:
            red_val += STEP_SIZE
        else:
            red_val -= STEP_SIZE

    if abs(green_val - target_green_val) >= STEP_SIZE:
        if target_green_val > green_val:
            green_val += STEP_SIZE
        else:
            green_val -= STEP_SIZE

    if abs(blue_val - target_blue_val) >= STEP_SIZE:
        if target_blue_val > blue_val:
            blue_val += STEP_SIZE
        else:
            blue_val -= STEP_SIZE
        
    color_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)
    print color_str
    
    requests.get(RGB_ENDPOINT, params={'rgb': color_str})
    
    time.sleep(DURATION)
    