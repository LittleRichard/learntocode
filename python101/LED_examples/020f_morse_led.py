import requests
import re
import time

# written by Jess Armstrong for coding101 round 1

SPACES_REGEX = r'[,\.\-\;\:\"\(\)\' ]+'

DOT = .1 # in seconds
DASH = DOT*3
REST = DOT
LETTER = DOT*2
SPACE = DOT*4
RGB_ENDPOINT = 'http://10.56.4.123:8934/blink1/fadeToRGB'

MORSE_DICT = {
	'a': (DOT, DASH),
	'b': (DASH, DOT, DOT, DOT),
	'c': (DASH, DOT, DASH, DOT),
	'd': (DASH, DOT, DOT),
	'e': (DOT,),
	'f': (DOT, DOT, DASH, DOT),
	'g': (DASH, DASH, DOT),
	'h': (DOT, DOT, DOT, DOT),
	'i': (DOT, DOT),
	'j': (DOT, DASH, DASH, DASH),
	'k': (DASH, DOT, DASH),
	'l': (DOT, DASH, DOT, DOT),
	'm': (DASH, DASH),
	'n': (DASH, DOT),
	'o': (DASH, DASH, DASH),
	'p': (DOT, DASH, DASH, DOT),
	'q': (DASH, DASH, DOT, DASH),
	'r': (DOT, DASH, DOT),
	's': (DOT, DOT, DOT),
	't': (DASH,),
	'u': (DOT, DOT, DASH),
	'v': (DOT, DOT, DOT, DASH),
	'w': (DOT, DASH, DASH),
	'x': (DASH, DOT, DOT, DASH),
	'y': (DASH, DOT, DASH, DASH),
	'z': (DASH, DASH, DOT, DOT)
}

red_val = 255
blue_val = 255
green_val = 255
null_val = 0

green_str = '#%.2x%.2x%.2x' % (null_val, green_val, null_val)
white_str = '#%.2x%.2x%.2x' % (red_val, green_val, blue_val)

col_input = raw_input('Please enter phrase you wish to convert to morsecode without numbers or special characters: ')

words_to_code = re.split(SPACES_REGEX, col_input)


requests.get(RGB_ENDPOINT, params={'rgb': white_str})
for word in words_to_code:
	lc_word = word.lower()
	print(word)

	for char in lc_word:
		print(char)
		if char in MORSE_DICT:
			for morse in MORSE_DICT[char]:
				if morse == DOT:
					print(' dot')
					requests.get(RGB_ENDPOINT, params={'rgb': green_str})
					time.sleep(DOT)
				elif morse == DASH:
					print(' dash')
					requests.get(RGB_ENDPOINT, params={'rgb': green_str})
					time.sleep(DASH)
				else:
					print('Invalid value in MORSE_DICT at key %s' % char)
				requests.get(RGB_ENDPOINT, params={'rgb': white_str})
				time.sleep(REST)
			time.sleep(LETTER)

		else:
			print('Invalid character skipped')
	time.sleep(SPACE)


