import random

# TODO:
# implement the `reversed` function built into python,
# without cheating and using the built-in function!!!
def my_reversed_negative(input_list):
    # there are a couple ways to do this, but either
    # way you need to know the length of the input
    # and that a range will spit out indices for you

    output_list = []
    len_input_list = len(input_list)
    for x in range(len_input_list):
        # make a negative index!
        idx = (x + 1) * -1
        output_list.append(input_list[idx])

    return output_list

# test it!
list1 = [1, 2, 3, 4, 5]
rev_list_neg = my_reversed_negative(list1)
print(f'{list1} reversed_negative: {rev_list_neg}')

def my_reversed_range(input_list):
    # this should be a bit simpler if we let
    # range do the heavy lifting

    output_list = []
    len_input_list = len(input_list)
    start_index = len_input_list - 1

    # range from length-of-list - 1 (index of final element)
    # to -1 (but not including -1!, so ends at zero), with
    # a step size of -1
    for x in range(start_index, -1, -1):
        output_list.append(input_list[x])

    return output_list

rev_list_range = my_reversed_range(list1)
print(f'{list1} reversed_range: {rev_list_range}')

# it's also possible to do via list comprehension...
# even though i asked for a function
list_comp = [
    list1[x] for x in range(len(list1) - 1, -1, -1)
]
print(f'{list1} list_comp {list_comp}')

# TODO:
# go back to your blackjack homework (or steal the solution)
# and modify it to use three functions:
# 1) a function that gets a random card (infinite deck)
# 2) a function that prints a card as human-readable
# 3) a function that retrieves a card's value
# hopefully these questions force you to consider which datatype
# you should use to represent the card in your logic!

# note how the complicated bits are much easier to follow

# BONUS: adjust blackjack to use a non-infinite deck, and
# make it play the game until you run out of cards.
def draw_card(num_suits=4, num_cards=13):
    # we use kwargs for the suit/card range; this
    # is a perfect use case because 99% of the time
    # we'll use the defaults, but it's easy to have
    # some flexibility too.
    suit_num = random.randint(1, num_suits)
    card_num = random.randint(1, num_cards)

    return (suit_num, card_num)

def get_card_value(card_num):
    if card_num == 1:
        card_value = 11
    elif card_num >= 10:
        card_value = 10
    else:
        card_value = card_num

    return card_value

def get_card_name(suit_num, card_num):
    if suit_num == 1:
        suit_name = 'Spades'
    elif suit_num == 2:
        suit_name = 'Clubs'
    elif suit_num == 3:
        suit_name = 'Diamonds'
    elif suit_num == 4:
        suit_name = 'Hearts'
    else:
        # only support 4 suits with names,
        # but dont break if we have more.
        suit_name = str(suit_num)

    if card_num == 1:
        card_name = 'Ace'
    elif card_num == 13:
        card_name = 'King'
    elif card_num == 12:
        card_name = 'Queen'
    elif card_num == 11:
        card_name = 'Jack'
    else:
        # will also print fine if i don't str() it
        card_name = str(card_num)

    return f'{card_name} of {suit_name}'


TARGET_TOTAL = 21
STARTING_CARDS = 2

# blackjack is a simple card game where
# you 'bust' if you go over TARGET_TOTAL.
cards_drawn = 0
cards_in_hand = []
hand_total = 0
num_aces = 0

# we could have drawn our cards outside the loop and then
# entered it for the user input, but we would have copy-pasted
# code to handle the first 2 cards being totaled... so instead
# we can make a more complicated while loop that is guaranteed
# to run at least the first STARTING_CARDS times without asking
# the user anything before going into the normal flow.
while hand_total < TARGET_TOTAL or cards_drawn < STARTING_CARDS:

    if cards_drawn >= STARTING_CARDS:
        # we've drawn our starting cards, now let
        # the player decide
        user_action = input(f'current total: {hand_total}. hit or stay? ')
    else:
        # if we're still drawing our first cards,
        # then we can use the 'hit' path
        user_action = 'hit'

    # NOTICE HOW: instead of having like 80 lines in the 'hit'
    # path and needing to scroll back and forth to read your code?
    # the functions have allowed us to compress code so that,
    # assuming our functions do what they say they do, the entire
    # action of getting the name of a card now only takes up one line
    #
    # We could take this a step further and implement a 'hit' function,
    # a 'double down' function, etc. The result would be that our
    # control flow logic (the loop and user input) would wrap a series
    # of function calls so that the heavy lifting of the actions' logic
    # is separated from the flow of our game, so BOTH components are
    # easier to follow.
    if user_action == 'hit' or user_action == 'h':
        # deal another card
        card_tuple = draw_card()
        cards_drawn += 1
        suit_num = card_tuple[0]
        card_num = card_tuple[1]

        card_name = get_card_name(suit_num, card_num)
        cards_in_hand.append(card_name)
        print(f'** got a {card_name}')

        card_value = get_card_value(card_num)
        hand_total += card_value
        if card_value == 11:
            num_aces += 1

        # if we would bust but we have an ace, convert
        # the ace from 11 -> 1 (subtract 10) and 'remove'
        # the ace
        if hand_total > TARGET_TOTAL and num_aces > 0:
            print('Converting an Ace to be worth 1')
            hand_total -= 10
            num_aces -= 1

    elif user_action == 'stay' or user_action == 's':
        # not hitting, which is also
        # an exit condition
        print('stay... probably a wise choice')
        break
    else:
        print(f'{user_action} is not valid, try again')
        # there is nothing else in this loop so i don't
        # need to handle this case, but if i had other stuff
        # after the else a `continue` would be appropriate

# this is a little hand-wavy math to make this
# silly print scale with TARGET_TOTAL.
# for target of 21 if you see 6 cards you probably
# busted, and 5 cards doesn't feel brave enough,
# so we land at 5.5
if TARGET_TOTAL / cards_drawn < 5.5:
    num_hits = cards_drawn - STARTING_CARDS
    print(f'you were very brave to hit {num_hits} times!')

print(f'you ended up with {", ".join(cards_in_hand)}')

if hand_total > TARGET_TOTAL:
    print(f'Busted, get em next time: {hand_total}')
elif hand_total == TARGET_TOTAL:
    if cards_drawn == STARTING_CARDS:
        print(f'BLACKJACK!!!')
    else:
        print(f'Nailed the {TARGET_TOTAL}!')
elif hand_total >= 18:
    print(f'Not bad! probably a winner: {hand_total}')
else:
    print(f'you got: {hand_total}')
