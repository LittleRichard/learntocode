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

# open a file and create the 'file_handle' variable
# to access it's contents
with open(PATH_TO_FILE) as file_handle:
    # the rest of this with-block is just an example of
    # how to iterate over the file text, so feel free
    # to use it or not depending on how you want to do these

    # ignore punctuation for now:
    # TODO: find the longest word in your text
    # TODO: find all words greater than 11 letters
    # TODO: how many times does a specific word appear?
    
    # then deal with punctuation
    # TODO: figure out how to strip punctuation
    # note that this is hard to do perfectly, just do
    # your best!

    # we don't have the right data structure to
    # count instances of words yet... womp womp.

    # .readlines() will iterate over the file,
    # with a loop for each time it encounters a 
    # new line character.
    for line in file_handle.readlines():

        # split the line on spaces, returns a list
        words_in_line = line.split(' ')
        for word in words_in_line:
            # when comparing things it is very typical
            # to 'normalize' your data; lowercasing everything
            # is a great way to make sure text is comparable.
            # .lower() will turn all characters into their 
            # lower case equivalent, assuming they have one.
            print(f'word: {word}, normalized: {word.lower()}')

# get another number of seconds since epoch time
end_time = time.time()
# diff them to get elapsed
elapsed_time = end_time - start_time
print(f'python took {elapsed_time} seconds to run this script')

# TODO: this is going to be an exercise in googling...
# write all words longer than 11 characters to a new file
# in descending order of length. first do it with duplicates,
# then make it unique.

OUTPUT_FILE = 'data/output.txt'
# modify the open() statement to enable write
with open(OUTPUT_FILE) as file_handle:
    pass

# BONUS: time other parts of your program! of all
# the TODOs, what is the slowest one?

# BONUS: dig into the slowest TODO, why is it slow?