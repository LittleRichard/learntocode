import os
import re
import random

# handling punctuation requires Regular Expressions, this one says
# to match on any group of what's in the square brackets. in this case,
# it's a mess of punctuation characters.
PUNCTUATION_AND_SPACES_REGEX = r'[,\.\-\;\:\"\(\)\' ]+'

def print_each_line_and_word(file_path):
    assert isinstance(file_path, str)

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

def find_longest_word(file_path):
    assert isinstance(file_path, str)

    # tell the operating system you want to read the file
    file_handle = open(file_path)

    longest_word = ''

    # loop over each line of the file
    for line in file_handle.readlines():
        # strip off the 'new line' character at the end
        line = line.strip('\n')
        # if this doesn't seem to work, try uncommenting this one too
        # line = line.strip('\r')

        # use Regular Expression to split on punctuation and whitespace
        words_in_line = re.split(PUNCTUATION_AND_SPACES_REGEX, line)
        for word in words_in_line:
            if len(word) > len(longest_word):
                # debug code
                #print(word)
                longest_word = word
    
    # this solution is incomplete, because what would happen
    # if the following line was your text?
    # I like peanut butter.
    # Answer: peanut (len of 6) would be selected, and
    # butter (also len 6) would be ignored because its not longer.
    # A better solution would be to track a list of all
    # words greater than or equal to some max length,
    # and return the whole list.
    return longest_word

def count_number_of_words(file_path):
    assert isinstance(file_path, str)

    # tell the operating system you want to read the file   
    file_handle = open(file_path)

    word_count = 0

    # loop over each line of the file
    for line in file_handle.readlines():
        # strip off the 'new line' character at the end
        line = line.strip('\n')
        # if this doesn't seem to work, try uncommenting this one too
        # line = line.strip('\r')

        words_in_line = re.split(PUNCTUATION_AND_SPACES_REGEX, line)
        word_count += len(words_in_line)

    return word_count

def count_specific_word(file_path, word_to_count):
    assert isinstance(file_path, str)
    assert isinstance(word_to_count, str)

    # tell the operating system you want to read the file   
    file_handle = open(file_path)
    lc_word_to_count = word_to_count.lower()

    word_count = 0

    # loop over each line of the file
    for line in file_handle.readlines():
        # strip off the 'new line' character at the end
        line = line.strip('\n')
        # if this doesn't seem to work, try uncommenting this one too
        # line = line.strip('\r')

        words_in_line = re.split(PUNCTUATION_AND_SPACES_REGEX, line)
        for word in words_in_line:
            if word.lower() == lc_word_to_count:
                word_count += 1

    return word_count

def get_lines_containing_word(file_path, word_to_find):
    assert isinstance(file_path, str)
    assert isinstance(word_to_find, str)

    # tell the operating system you want to read the file   
    file_handle = open(file_path)
    lc_word_to_find = word_to_find.lower()

    matching_lines = [] # an empty list

    # loop over each line of the file
    for line in file_handle.readlines():
        # strip off the 'new line' character at the end
        line = line.strip('\n')
        # if this doesn't seem to work, try uncommenting this one too
        # line = line.strip('\r')

        words_in_line = re.split(PUNCTUATION_AND_SPACES_REGEX, line)
        for word in words_in_line:
            if word.lower() == lc_word_to_find:
                matching_lines.append(line)
                # what happens if there are multiple of the same word?
                # answer: this would append duplicate lines, one
                # for each match... can you think of a way around it?

    return matching_lines

def get_count_of_all_words(file_path):
    assert isinstance(file_path, str)

    # we'll need a different data structure to do this efficiently,
    # tuples/lists are a crappy way to store this data.
    # instead, let's use a dictionary

    return 'dont try it without dictionaries'

# be sure to make a directory next to this script
# called 'text_files' to hold all your sample texts.
#FILE_PATH = 'text_files/file_name_to_parse.txt' 
FILE_PATH = 'text_files/bible.txt'

if not os.path.isfile(FILE_PATH):
    print('not a valid file path: %s' % FILE_PATH)
    exit()

# TODO call your functions against the specified file text
longest_word = find_longest_word(FILE_PATH)
print('The longest word is %s' % longest_word)

num_words = count_number_of_words(FILE_PATH)
print('Total %s words' % num_words)

word_to_count = 'God'
num_of_a_word = count_specific_word(FILE_PATH, word_to_count)
print('The word %s was found %s times' % (word_to_count, num_of_a_word))

word_to_find = 'Satan' 
lines = get_lines_containing_word(FILE_PATH, word_to_find)
print('Matched %s in %s lines, examples:' % (word_to_find, len(lines)))
for line in lines[:8]:
    print(line)