import os
import re
import random
import pprint

# handling punctuation requires Regular Expressions, this one says
# to match on any group of what's in the square brackets. in this case,
# it's a mess of punctuation characters.
PUNCTUATION_AND_SPACES_REGEX = r'[,\.\-\;\:\"\(\)\' ]+'

def print_each_line_and_word(file_path):

    # tell the operating system you want to read the file
    file_handle = open(file_path)

    # loop over each line of the file
    for line in file_handle.readlines():
        # strip off the 'new line' character at the end
        line = line.strip('\n')
        # if this doesn't seem to work, try uncommenting this one too
        # line = line.strip('\r')
        # for example, we can print each line
        print(line)

        # use Regular Expression to split on punctuation and whitespace
        words_in_line = re.split(PUNCTUATION_AND_SPACES_REGEX, line)

        for word in words_in_line:
            print(word)

def get_count_of_all_words(file_path):
    # return a dictionary where each word is the key
    # and the value is the number of times the word is found

    return {} # TODO

# be sure to make a directory next to this script
# called 'text_files' to hold all your sample texts.
#FILE_PATH = 'text_files/file_name_to_parse.txt' 
FILE_PATH = 'text_files/bible.txt'

if not os.path.isfile(FILE_PATH):
    print('not a valid file path: %s' % FILE_PATH)
    exit()

count_by_word = get_count_of_all_words(FILE_PATH)

pprint.pprint(count_by_word) # HUGE print statement

# TODO: now that you have the count by word, do something
# interesting with it.  What data can you mine?