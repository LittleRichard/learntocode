

print("""
At long last, we have all the tools to do things I've
hinted at in past homeworks!
""")

# TODO: prove that the most likely sum of rolling
# two dice of the same size is 1 + the number of sides.
# hints: 
# - use a loop to do a million random iterations
# - use a dictionary with key as sum-of-dice, value is the count.
# - try it for a few different dice sizes
DICE_SIZE = 6


# TODO: choose 5 words. find all line numbers where
# those words appear and store them (per-word) in
# a dictionary. print the result, which should look
# something like:
# 'hemoglobin' appears 3 times, at lines 5, 282, 1005

# here's the file iteration code for free, modify
# as necessary
PATH_TO_FILE = 'data/dracula_sample.txt'
with open(PATH_TO_FILE) as file_handle:
    for line in file_handle.readlines():
        words_in_line = line.split(' ')

        # this is a fast way to strip punctuation.
        # it makes a translation object that knows
        # how to replace punctuation with empty strings.
        # This is object-oriented code, which we
        # won't really cover here.
        line = line.translate(
            str.maketrans('', '', string.punctuation))

        for word in words_in_line:
            pass 

# the pprint library might be convenient

