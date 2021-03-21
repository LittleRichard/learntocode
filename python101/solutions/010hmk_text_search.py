import string
import time

print("""
    we're going to see a few new tools here, some of
    which i've provided and some of which you'll
    find and figure out on your own!
    - opening and consuming files
    - splitting strings
    - replacing data in strings
    - timing things
    - writing files

    the script with example logic techniques may help you
  
    example code is provided, but expect to do
    some googling to figure out how to do similar
    actions that might help you.
""")

# this is a path just like you would see if you
# did a `pwd` in the terminal, and is relative
# to wherever you are when you execute the program,
# NOT your script itself!
PATH_TO_FILE = 'data/dracula_sample.txt'

# this file is included in the repo; it is safe from
# copyright because its so old the copyright expired.
# feel free to add your own files with any data you want,
# BUT DONT COMMIT CONTENT YOU DONT OWN.
# the bible is a particularly good one for this case
print('bigger files will be more interesting')

# the 'with <something>' block tells python to do some 
# special handling with <something> once we're done with
# it. Critically, the 'cleanup' step happens even if an
# error is thrown inside the block.
# in the case of opening a file, this helps the OS
# know to block and release access to the file.

# time.time() returns a number describing the number
# of seconds since January 1, 1970, AKA 'epoch time'
start_time = time.time()
time_strip_punc = 0
time_lowercasing = 0
time_append = 0

# open a file and create the 'file_handle' variable
# to access it's contents
with open(PATH_TO_FILE) as file_handle:
    # the rest of this with-block is just an example of
    # how to iterate over the file text, so feel free
    # to use it or not depending on how you want to do these

    # ignore punctuation for now:
    # TODO: find the longest word in your text
    longest_word = ''
    # TODO: find all words greater than 13 letters
    big_words = []
    BIG_WORD_SIZE = 13
    # TODO: how many times does a specific word appear?
    search_word = 'transylvania'
    search_word_count = 0
    
    # then deal with punctuation
    # TODO: figure out how to strip punctuation
    # note that this is hard to do perfectly, just do
    # your best!
    punc_chars = string.punctuation
    # add the newline character, it was getting in the way
    # for the text i used; this may or may not affect you!
    punc_chars += '\n'  

    # TODO:
    # we don't have the right data structure to
    # count instances of words yet... womp womp.
    # BUT you can still adjust your 'find longest word'
    # code to instead find ALL of the longest words,
    # instead of just the first word you see of that
    # length.
    longest_words = []

    # .readlines() will iterate over the file,
    # with a loop for each time it encounters a 
    # new line character.
    for line in file_handle.readlines():

        # split the line on spaces, returns a list
        words_in_line = line.split(' ')
        for word in words_in_line:
            lower_word_start = time.time()
            lower_word = word.lower()
            time_lowercasing += (time.time() - lower_word_start)

            # remove punctuation. there are more efficient
            # ways but this one uses tools we already know.
            # this is where i'd start if i was making my
            # script run faster.
            strip_punc_start = time.time()
            lower_word = ''.join(
                x for x in lower_word if x not in punc_chars)
            time_strip_punc += (time.time() - strip_punc_start)

            if len(lower_word) > len(longest_word):
                longest_word = lower_word
                longest_words = []  # blank out the list
                
                start_append = time.time()
                longest_words.append(lower_word)  # add this word
                time_append += (time.time() - start_append)
            elif len(lower_word) == len(longest_word):
                start_append = time.time()
                longest_words.append(lower_word)
                time_append += (time.time() - start_append)

            if len(lower_word) > BIG_WORD_SIZE:
                start_append = time.time()
                big_words.append(lower_word)
                time_append += (time.time() - start_append)

            if lower_word == search_word:
                search_word_count += 1

print('')
print(f'longest_word: {longest_word}')
print(f'longest_words: {longest_words}')
print(f'big_words: {big_words}')
print(f'"{search_word}" appears {search_word_count} times')

# get another number of seconds since epoch time
end_time = time.time()
# diff them to get elapsed
elapsed_time = end_time - start_time
print(f'python took {elapsed_time} seconds to run this script')

# TODO: this is going to be an exercise in googling...
# write all words longer than BIG_WORD_SIZE characters to a new file
# in descending order of length. first do it with duplicates,
# then make it unique.

# de-duplicate the list (there are better ways, soon)
de_duped_fifteen = []
for x in big_words:
    if x not in de_duped_fifteen:
        de_duped_fifteen.append(x)

OUTPUT_FILE = 'data/output.txt'
# modify the open() statement to enable write
with open(OUTPUT_FILE, 'w') as file_handle:
    file_handle.write('\n'.join(de_duped_fifteen))

print(f'see results in {OUTPUT_FILE}')

# BONUS: time other parts of your program! of all
# the TODOs, what is the slowest one?
# hint: to really see a difference, find a bigger 
# text file... or find a way to create a bigger
# file by copying the one you already have?
print(f'spent stripping punctuation: {time_strip_punc}')
strip_punc_perc_total = 100 * time_strip_punc / elapsed_time
print(f'% of total time stripping punc: {strip_punc_perc_total}')

print(f'spent lowercasing: {time_lowercasing}')
lowercasing_perc_total = 100 * time_lowercasing / elapsed_time
print(f'% of total time lowercasing: {lowercasing_perc_total}')

print(f'spent appending: {time_append}')
append_perc_total = 100 * time_append / elapsed_time
print(f'% of total time appending: {append_perc_total}')

# BONUS: dig into the slowest TODO, why is it slow?
# - other than reading the file, the slowest operation
#   is probably going to be all the 'normalizing' and pre-processing
#   of the lines/words as you iterate. this is because creating
#   and analyzing strings in python can be really slow...
# - you probably noticed that all the logic to check lengths/sizes
#   is really fast; integer comparison and addition is really fast!
# - if you remember the 'why list comprehension is fast' from class,
#   (depending on the size of your file) you may have also noticed 
#   that the 'append' takes time as well. if you append < 100 times,
#   you definitely won't see it, but for huge data sets you might.
#   this is partially because we're appending a lot, but
#   if you dig in further... you may have noticed that MOST of the 
#   .append() calls are fast, but once in a while one will be way slower.
#   the slow ones are when python needs to re-allocate memory because
#   the list has grown!