import os
import re

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

def count_number_of_words(file_path):
    assert isinstance(file_path, str)

    # return a count of the number of words in the
    # text of the given file path

    return 'TODO'

def count_specific_word(file_path, word_to_count):
    assert isinstance(file_path, str)
    assert isinstance(word_to_count, str)

    # return a count of how many times the given
    # word appears in the text of the file path

    return 'TODO'

def find_longest_words(file_path):
    assert isinstance(file_path, str)
    # return a list with either the
    # single longest word, or (more likely)
    # all words that are tied for the longest word

    return 'TODO'

def get_lines_containing_word(file_path, word_to_find):
    assert isinstance(file_path, str)
    assert isinstance(word_to_count, str)
    # return a list of all lines containing the given
    # word found in the text of the given file path

    return 'TODO'

def get_count_of_all_words(file_path):
    # return a dictionary mapping each word found
    # in the text to the number of times that word is found.

    # we'll need a different data structure to do this efficiently,
    # tuples/lists are a crappy way to store this data.
    return 'dont try it yet'

# be sure to make a directory next to this script
# called 'text_files' to hold all your sample texts.
#FILE_PATH = 'text_files/file_name_to_parse.txt' 
FILE_PATH = 'text_files/bible.txt'

if not os.path.isfile(FILE_PATH):
    print('not a valid file path: %s' % FILE_PATH)
    exit()

# TODO call your functions against the specified file text
print_each_line_and_word(FILE_PATH)
