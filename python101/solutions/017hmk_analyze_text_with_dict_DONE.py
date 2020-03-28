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

    # tell the operating system you want to read the file
    file_handle = open(file_path)

    count_by_word = {}

    # loop over each line of the file
    for line in file_handle.readlines():
        # strip off the 'new line' character at the end
        line = line.strip('\n')
        # if this doesn't seem to work, try uncommenting this one too
        # line = line.strip('\r')

        # use Regular Expression to split on punctuation and whitespace
        words_in_line = re.split(PUNCTUATION_AND_SPACES_REGEX, line)

        for word in words_in_line:
            lowercase_word = word.lower() # normalize the text for lookup in the dict

            if lowercase_word in count_by_word:
                # increment the value for that word (the counter) by 1
                count_by_word[lowercase_word] = count_by_word[lowercase_word] + 1
            else:
                # first time we've found it, add it to the dict
                count_by_word[lowercase_word] = 1

    return count_by_word

def get_count_of_specific_words(count_by_word, words_to_find):
    # return a dict with keys of the given words_to_print
    # and values of the number of times it was found
    assert isinstance(count_by_word, dict)
    assert isinstance(words_to_find, (tuple, list))

    return_dict = {}

    for word in words_to_find:
        lowercase_word = word.lower()

        if lowercase_word in count_by_word:
            return_dict[word] = count_by_word[lowercase_word]
        else:
            return_dict[word] = 0

    return return_dict

def filter_counted_words(count_by_word, min_word_length, min_appearances):
    # returns a dict that is a subset of the given count_by_word,
    # with only words equal-or-longer than the given min_word_length
    # and appearing min_appearances or more times.
    assert isinstance(count_by_word, dict)
    assert isinstance(min_word_length, int)
    assert isinstance(min_appearances, int)

    return_dict = {}

    for word, count in count_by_word.iteritems():
        if len(word) >= min_word_length and count >= min_appearances:
            return_dict[word] = value

    return return_dict

# be sure to make a directory next to this script
# called 'text_files' to hold all your sample texts.
#FILE_PATH = 'text_files/file_name_to_parse.txt' 
FILE_PATH = 'text_files/bible.txt'

if not os.path.isfile(FILE_PATH):
    print('not a valid file path: %s' % FILE_PATH)
    exit()

count_by_word = get_count_of_all_words(FILE_PATH)

# HUGE print statement
# pprint.pprint(count_by_word) 

my_words = ('dict', 'tree', 'million',
            'god', 'jesus', 'satan',
            'methuselah', 'apple', 'snake')
print('Filtering by specific words')
count_specific_words_dict = get_count_of_specific_words(count_by_word, my_words)
for key, value in count_specific_words_dict.iteritems():
    if value > 0:
        print('%s found %s times' % (key, value))
    else:
        print('NOT FOUND: %s' % key)
print('')

print('Filtering by minimum word length and appearances')
filtered_count_by_word = filter_counted_words(count_by_word, 10, 100)
for key, value in filtered_count_by_word.iteritems():
    print('%s found %s times' % (key, value))
print('')