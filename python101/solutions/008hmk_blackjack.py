import random

# play a game of blackjack with 1 player

# we don't have a great way of removing cards
# from a deck (yet), so assume you have an 
# infinite deck of cards,

# prompt for input to hit or stay
# implement failure conditions
# do your best with handling the ace as 1 or 11

# you will probably copy-paste if-trees,
# and there is a better way that we haven't
# seen yet (making your own function)

# BONUS: could you adjust your game to take
# turns with an opponent? an entire table?
# it might be easier than you think!
print("""
Multiplayer not implemented in this script to
focus on the game logic, but it's easy!

for x in range(num_players):
    <highlight your game's entire loop and hit tab to indent it>

    # adjust it a little bit to print whose
    # turn it is, if you want to make person
    # the dealer and beat them, etc.
""")

# BONUS: BONUS: casinos never close, how can
# you make your blackjack table stay open?
print("""
Casino mode also not implemented in this script to
focus on the game logic, but it's also easy!

while True:  # run forever
    for x in range(num_players):
        <your game is still in the for loop>

    <any summary of the game>

    # when a game ends, we go right
    # back to the top of the loop!
""")


print("Let's play blackjack!")

TARGET_TOTAL = 21
STARTING_CARDS = 2

# blackjack is a simple card game where
# you 'bust' if you go over TARGET_TOTAL.
cards_drawn = 0
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

    if user_action == 'hit' or user_action == 'h':
        # deal another card
        hit_card = random.randint(1, 13)
        cards_drawn += 1

        # copied from previous homework and modified
        if hit_card == 1:
            card_name = 'Ace'
            card_value = 11
            num_aces += 1
        elif hit_card == 13:
            card_name = 'King'
            card_value = 10
        elif hit_card == 12:
            card_name = 'Queen'
            card_value = 10
        elif hit_card == 11:
            card_name = 'Jack'
            card_value = 10
        else:
            # will also print fine if i don't str() it
            card_name = str(hit_card)
            card_value = hit_card

        print(f'** got a {card_name}')
        
        hand_total += card_value

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
