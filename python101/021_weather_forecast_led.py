import time
import datetime
import requests
import pprint

RGB_ENDPOINT = 'http://10.56.1.126:8934/blink1/fadeToRGB'

WEATHER_ENDPOINT = 'http://api.openweathermap.org/data/2.5/forecast'
WEATHER_API_KEY = '23c42c4325e2a41669c88952a290afb6'

ZIP_CODE_STR = '02135'
HOURS_IN_FUTURE_TO_EXAMINE = 75
MIN_SIGNIFICANT_PRECIPITATION_MM = 1
DOWNLOAD_DATA_INTERVAL_MINUTES = 1

NO_BLINK_SLEEP_SECONDS = 60
MAX_BLINK_INTERVAL_SECONDS = 2.5
MIN_BLINK_INTERVAL_SECONDS = .5
BLINK_DURATION_SECONDS = .2
BRIGHTNESS_VARIANCE = .7
assert 0 <= BRIGHTNESS_VARIANCE <= 1

def set_led_to_color(red_val, green_val, blue_val):
    assert isinstance(red_val, int)
    assert 0 <= red_val <= 255, red_val
    assert isinstance(green_val, int)
    assert 0 <= green_val <= 255, green_val
    assert isinstance(blue_val, int)
    assert 0 <= blue_val <= 255, blue_val

    color_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)

    my_payload = {'rgb': color_str}

    try:
        requests.get(RGB_ENDPOINT, params=my_payload)
    except Exception as exc:
        print('Error setting data... %s', exc)

def get_weather_for_zip_code(zip_code_str):
    assert isinstance(zip_code_str, basestring)
    # should be all numbers, so we'll just try it
    try:
        int(zip_code_str)
    except:
        assert False, zip_code_str

    response = requests.get(
                            WEATHER_ENDPOINT,
                            params={
                                'APPID': WEATHER_API_KEY,
                                'zip': zip_code_str,
                                'units': 'imperial',
                            })

    return response.json()

def get_percentage_within_range(value, min_val, max_val):
    """
        Returns a float that is >= 0 and <= 1.0.
        0 would mean the L{value} is equal to or less than L{min_val}.
        1 would mean the L{value} is equal to or greater than L{max_val}.
    """
    adjusted_value = min(max(min_val, value), max_val) # pins the value within the range
    return float(adjusted_value - min_val) / (max_val - min_val)

def get_led_value_from_weather(num_hours_in_future):

    now_datetime = datetime.datetime.now()
    cutoff_time = now_datetime + datetime.timedelta(hours=num_hours_in_future)

    max_cloudiness = 0
    num_windows_viewed = 0
    total_temp = 0

    times_with_rain = []

    print 'fetching weather data at %s' % now_datetime
    all_weather_dict = get_weather_for_zip_code(ZIP_CODE_STR)    

    for weather_at_time in all_weather_dict['list']:
        num_windows_viewed += 1

        weather_datetime = datetime.datetime.fromtimestamp(weather_at_time['dt'])
        if weather_datetime >= cutoff_time:
            break

        total_temp += weather_at_time['main']['temp']

        max_cloudiness = max(max_cloudiness, weather_at_time['clouds']['all'])

        if 'rain' in weather_at_time and '3h' in weather_at_time['rain']:
            if weather_at_time['rain']['3h'] >= MIN_SIGNIFICANT_PRECIPITATION_MM:
                times_with_rain.append(weather_datetime)
                # pprint.pprint(weather_at_time)

        elif 'snow' in weather_at_time and '3h' in weather_at_time['snow']:
            if weather_at_time['snow']['3h'] >= 10 * MIN_SIGNIFICANT_PRECIPITATION_MM:
                times_with_rain.append(weather_datetime)

    if num_windows_viewed == 0:
        print('no data found...')
        return (0,0,0,0)

    average_temp = float(total_temp) / num_windows_viewed

    # red should be zero at lower temp, and highest at the top of the range
    red_val = 255 * get_percentage_within_range(average_temp, 50, 100) 

    # green should be strongest in the middle of the range,
    # and lowest at the edges.
    green_perc = get_percentage_within_range(average_temp, 25, 75)
    if green_perc >= .5:
        green_val = 255 * (2 * (1 - green_perc))
    else:
        green_val = 255 * (2 * green_perc)

    print('avg temp %s, green_perc %s, green val %s' % (average_temp, green_perc, green_val))

    # blue should be highest at the bottom of the range, and zero at the top
    blue_val = 255 * (1 - get_percentage_within_range(average_temp, 0, 50))

    # brightness should run from .5 for max cloudiness up to
    # full strength for no clouds
    brightness = 1 - (BRIGHTNESS_VARIANCE * (.01 * max_cloudiness))
    red_val = int(brightness * red_val)
    green_val = int(brightness * green_val)
    blue_val = int(brightness * blue_val)

    if times_with_rain:
        soonest_rain = min(times_with_rain)
        timedelta_to_rain = soonest_rain - now_datetime
        time_to_rain_in_hours = timedelta_to_rain.total_seconds() / 60.0 / 60.0 + 1 # +1 so that rain now will blink fastest
        percentage_of_future_time_range = float(HOURS_IN_FUTURE_TO_EXAMINE - time_to_rain_in_hours) / HOURS_IN_FUTURE_TO_EXAMINE

        # blink interval should be fastest with rain/snow soon, slowing to off if there is none
        # in the forecast
        blink_interval = MAX_BLINK_INTERVAL_SECONDS * (1 - min(1, max(percentage_of_future_time_range, 0)))
        blink_interval = max(blink_interval, MIN_BLINK_INTERVAL_SECONDS)
    else:
        blink_interval = 0

    return (red_val, green_val, blue_val, blink_interval)

data_fetch_interval_in_min = datetime.timedelta(minutes=15)
# init to a value that will trigger the first time
last_time_fetched = datetime.datetime.now() - data_fetch_interval_in_min

while True:
    # pprint.pprint(all_weather_dict['list'][0])

    now_datetime = datetime.datetime.now()
    if now_datetime >= (last_time_fetched + data_fetch_interval_in_min):
        (
         red_val, 
         green_val, 
         blue_val, 
         blink_interval, # zero if should not blink
         ) = get_led_value_from_weather(HOURS_IN_FUTURE_TO_EXAMINE)

        last_time_fetched = now_datetime
        print red_val, green_val, blue_val
        set_led_to_color(red_val, green_val, blue_val)

    if blink_interval:
        print('blink every %s seconds' % blink_interval)
        set_led_to_color(0,0,0)
        time.sleep(BLINK_DURATION_SECONDS)
        set_led_to_color(red_val, green_val, blue_val)
        time.sleep(blink_interval)
    else:
        print 'no blink, sleep %s' % NO_BLINK_SLEEP_SECONDS
        time.sleep(NO_BLINK_SLEEP_SECONDS)


    
    
