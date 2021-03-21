import random

# a quick last thing with cards

print("""
    Did you make a list of numbers 1-52, 
    shuffle, and then convert to human-readable
    on the way out? Or did you make them human
    readable before you shuffled them?

    In this example, it doesn't matter, but...
    always consider how to store data carefully!!!

    2 examples:
    - If we needed to sort it, the computer would
      handle numbers a lot more quickly than strings
      so at scale (think 100k+ things) there 
      could be huge difference.
    - If we need to figure out if it was a good poker
      hand, it would probably be a lot easier with
      numbers as well.
""")

# TODO: fill a list with 52 unique cards
deck = [x for x in range(1, 53)]

# another way you could represent cards is a list of
# tuples, where each tuple has (<suit_num>, <card_num>)
tuple_cards_deck = [
    (random.randint(1, 4), random.randint(1, 13))
]

# TODO: google your way to using the random library
# to shuffle the list of cards
random.shuffle(deck)

# TODO: deal a hand of 5 cards and print it
print('your hand is: ')
# since i've shuffled, i can just grab the first 5
# and they'll be random
for x in deck[:5]:

    # hopefully by now you're getting sick of
    # copy-pasting this code... next class we'll
    # fix it.

    # +1 because remainders are 0-12
    card_num = (x % 13) + 1 
    suit_num = (x % 4) + 1

    if suit_num == 1:
        suit_name = 'Spades'
    elif suit_num == 2:
        suit_name = 'Clubs'
    elif suit_num == 3:
        suit_name = 'Diamonds'
    else:
        # we know that it can only be a 4 here, but
        # assumptions like this are how bugs creep in.
        # if line 13 ever changes... who knows?
        suit_name = 'Hearts'

    # same about if, if, if... vs if-elif-elif-elif...
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

    print(f'{card_name} of {suit_name}')
