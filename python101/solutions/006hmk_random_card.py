import random # import is how you tell python that you want to use a library in a script

# TODO: simulate a roll of a 4-sided die, print the result
die4 = random.randint(1, 4)
print(f'4-sided: {die4}')

# TODO: simulate a roll of a 13-sided die, print the result
die13 = random.randint(1, 13)
print(f'13-sided: {die13}')

# TODO: simulate drawing a single card from a standard 52-card deck
rand_card = random.randint(1, 13)  # AKA die13
rand_suit = random.randint(1, 4)  # AKA die4

# this would work if these were all if statements and
# not an if-elif-elif, but it's incorrect; there
# should only be one outcome here because these events
# are linked together.
if rand_suit == 1:
    suit_name = 'Spades'
elif rand_suit == 2:
    suit_name = 'Clubs'
elif rand_suit == 3:
    suit_name = 'Diamonds'
else:
    # we know that it can only be a 4 here, but
    # assumptions like this are how bugs creep in.
    # if line 13 ever changes... who knows?
    suit_name = 'Hearts'

# same about if, if, if... vs if-elif-elif-elif...
if rand_card == 1:
    card_name = 'Ace'
elif rand_card == 12:
    card_name = 'King'
elif rand_card == 11:
    card_name = 'Queen'
elif rand_card == 10:
    card_name = 'Jack'
else:
    # will also print fine if i don't str() it
    card_name = str(rand_card)

print(f'Your random card is the {card_name} of {suit_name}')

if rand_card == 13 and rand_suit == 1:
    print('THE ACE OF SPADES!')
