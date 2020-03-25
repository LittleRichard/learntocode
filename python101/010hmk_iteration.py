import time
import random

NUM_ITERS = 10000

start_time = time.time() # returns a float, the number of seconds since 'epoch time': Jan 1, 1970 00:00:00
# instead of making a tuple out of our xrange, we can just use the xrange as our for-loop's iterable!

# TODO: write a for-loop that will iterate NUM_ITERS times.
# each time it should:
## roll a 10,000-sided die
## if the rolled value is equal to 42, print the current loop number
## to test, you'll probably have to make your NUM_ITERS value big...


# print the time elapsed
time_elapsed = time.time() - start_time
print('%s iterations took %.3f seconds' % (NUM_ITERS, time_elapsed))


NUM_DICE = 100000
DICE_MIN_VAL = 1
NUM_SIDES = 22

start_time = time.time()
# Copy-paste your for loop from above here
# TODO: modify it to calculate the average value of dice rolls
## Hint: as always, first think about what you need to calculate
## the average value, and once you know what you need, it 
## should be easier to figure out how you'll get it.
## An average is (total / attempts), how would you get the total?


time_elapsed = time.time() - start_time
print('%s iterations took %.3f seconds' % (NUM_DICE, time_elapsed))

# observe how increasing the NUM_DICE makes the average result converge to the average
# that we'd expect by doing math!

# sum all possible dice values
all_die_values = xrange(DICE_MIN_VAL, (NUM_SIDES + 1))
# divide by number of sides to get the average
die_average = float(sum(all_die_values)) / NUM_SIDES
print('Mathematical average is %s' % die_average)


# And finally, steal code from the last homework's solution to make this 
# double for-loop print every card in a 52 card deck.
## hint: select multiple lines and hit 'tab' to bulk-indent
## hint: in sublime, ctrl+H gives you the find-and-replace menu