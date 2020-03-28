import time
import random

NUM_ITERS = 100000
NUM_BIG_DICE_SIDES = 100000
NUM_DICE = 100000
DICE_MIN_VAL = 1
NUM_SMALL_DICE_SIDES = 22

start_time = time.time() # returns a float, the number of seconds since 'epoch time': Jan 1, 1970 00:00:00
# instead of making a tuple out of our xrange, we can just use the xrange as our for-loop's iterable!

# TODO: write a for-loop that will iterate NUM_ITERS times.
# each time it should:
## roll a 100,000-sided die
## if the rolled value is equal to 42, print the current loop number
for iter_num in xrange(1, NUM_ITERS + 1):
    # roll a 100000-sided die
    dice_roll = random.randint(DICE_MIN_VAL, NUM_BIG_DICE_SIDES)
    if dice_roll == 42:
        print('nailed it on iteration number %s' % iter_num)

# print the time elapsed
time_elapsed = time.time() - start_time
print('%s iterations took %.3f seconds' % (NUM_ITERS, time_elapsed))


# Copy-paste your for loop from above here
# TODO: modify it to calculate the average value of dice
running_total = 0

start_time = time.time()
for iter_count in xrange(NUM_DICE):
    die_val = random.randint(DICE_MIN_VAL, NUM_SMALL_DICE_SIDES)
    running_total = running_total + die_val

time_elapsed = time.time() - start_time
print('%s iterations took %.3f seconds' % (NUM_DICE, time_elapsed))

# observe how increasing the NUM_DICE makes the average result converge to the average
# that we'd expect by doing math!
all_die_values = xrange(DICE_MIN_VAL, (NUM_SMALL_DICE_SIDES + 1))
die_average = float(sum(all_die_values)) / NUM_SMALL_DICE_SIDES

print('Total is %s.  Average is %s, expected average is %s' % (
                                                               running_total,
                                                               float(running_total) / NUM_DICE,
                                                               die_average, # math calculated average
                                                               )
      )


# And finally, steal code from the last homework's solution to make this 
# double for-loop print every card in a 52 card deck.
## hint: select multiple lines and hit 'tab' to bulk-indent
## hint: in sublime, ctrl+H gives you the find-and-replace menu
for suit in xrange(1,5):
    for card in xrange(1,14):
        # in this instance, does it matter
        # if we put the card or suit loop on the outside?
        # not to satisfy the assignment, but the output
        # would be different.  Ace/Spaces, Two/Spades ...
        # versus Ace/Spades, Ace/Clubs, Ace/Hearts...

        if card == 1:
            card_name = 'Ace'
        elif 2 <= card <= 10:
            card_name = card
        elif card == 11:
            card_name = 'Jack'
        elif card == 12:
            card_name = 'Queen'
        else:
            card_name = 'King'

        if suit == 1:
            suit_name = 'Spades'
        elif suit == 2:
            suit_name = 'Clubs'
        elif suit == 3:
            suit_name = 'Diamonds'
        else:
            suit_name = 'Hearts'

        print('Your card is the %s of %s' % (card_name, suit_name))