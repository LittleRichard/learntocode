import random

# create a function that accepts 2 arguments:
## a card number
## a suit number
# assert that the values are
## the right types
## in the range you expect
# DO NOT put any code in your function yet!
def get_card_name(card, suit):
    assert isinstance(card, int)
    assert isinstance(suit, int)

    assert 1 <= card <= 13, card
    assert 1 <= suit <= 4, suit

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

    card_name = 'Your card is the %s of %s' % (card_name, suit_name)
    return card_name


# move the logic from the 'print a card' assignment
# into your function above.  Use the input arguments and
# return the card's name as:
## 'CARD_NAME of SUIT_NAME'
## example: 'Jack of Clubs'





# use your function to print every card in a 
# 52-card deck
print('printing all cards in deck')
for card_num in xrange(1,14):
    for suit_num in xrange(1,5):
        card_name = get_card_name(card_num, suit_num)
        print(card_name)
print('')


# use your function to draw a random hand
# of 5 cards and print it. Don't worry about handling 
# drawing unique cards, you might pull the same one twice
## data structures we haven't seen, lists, sets, and dictionaries,
## will make this really easy.
print('your hand is:')
for x in xrange(5):
    rand_card_num = random.randint(1,13)
    rand_suit_num = random.randint(1,4)
    card_name = get_card_name(rand_card_num, rand_suit_num)
    print(card_name)


# once you can use lists, we can eliminate duplicates
my_hand = []
while len(my_hand) < 5: # keep going until the hand is full
    rand_card_num = random.randint(1,13)
    rand_suit_num = random.randint(1,4)
    card_name = get_card_name(rand_card_num, rand_suit_num)
    # check if the random card has already been pulled out of the deck,
    # and only add it to the list representing my hand if it's not
    # already in there
    if card_name not in my_hand: 
        my_hand.append(card_name)
print('')

print('your non-duplicate hand is:')
for my_card in my_hand:
    print(my_card)