import pprint
import random
import string

print("""
At long last, we have all the tools to do things I've
hinted at in past homeworks!
""")

# TODO: prove that the most likely sum of rolling
# two dice of the same size is 1 + the number of sides.
# hints: 
# - use a loop to do a million iterations
# - use a dictionary with key as sum-of-dice, value is the count.
# - try it for a few different dice sizes
NUM_SIDES = 6
NUM_ITERS = 10000 

sum_to_count = dict()

for x in range(NUM_ITERS):
    dice_sum = (random.randint(1, NUM_SIDES) +
                random.randint(1, NUM_SIDES)) 

    if dice_sum not in sum_to_count:
        sum_to_count[dice_sum] = 0

    # could have done an else where we set it to
    # 1, but i like initializing the value
    # and then letting the increment path happen
    # just like it would if the value was already
    # present in the dict
    sum_to_count[dice_sum] += 1

# sometimes you need to be more specific
# when using sorted, but in this case it does
# what i want and sorts by keys.
for key, value in sorted(sum_to_count.items()):
    print(f'sum {key}, count {value}')

# TODO: choose 5 words. find all line numbers where
# those words appear and store them (per-word) in
# a dictionary. print the result, which should look
# something like:
# 'hemoglobin' appears 3 times, at lines 5, 282, 1005

WORDS_SET = set((
    'transylvania',
    'carpathians',
    'vampire',
    'and',
    'or'
))

lines_by_word = {}

# here's the file iteration code for free, modify
# as necessary
PATH_TO_FILE = 'data/dracula_sample.txt'
with open(PATH_TO_FILE) as file_handle:

    line_num = 0
    # some of you may have found the 'enumerate'
    # builtin function; that's cool too!
    for line in file_handle.readlines():
        line_num += 1

        # this is a fast way to strip punctuation.
        # it makes a translation object that knows
        # how to replace punctuation with empty strings.
        # This is object-oriented code, which we
        # won't really cover here.
        line = line.translate(
            str.maketrans('', '', string.punctuation))

        for word in line.split(' '):
            lower_word = word.lower()
            if lower_word in WORDS_SET:
                if lower_word not in lines_by_word:
                    lines_by_word[lower_word] = []

                lines_by_word[lower_word].append(line_num)


print(f'text search results:')
pprint.pprint(lines_by_word)