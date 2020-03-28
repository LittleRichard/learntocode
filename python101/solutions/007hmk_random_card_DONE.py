import random # import is how you tell python that you want to use a library in a script

# a similar function, but for floats.  It takes no inputs
my_rand_card = random.randint(1, 13) # returns a value: 1 <= X <= 13
my_rand_suit = random.randint(1, 4) # returns a value: 1 <= X <= 4

if my_rand_card == 1:
	card_name = 'Ace'
elif 2 <= my_rand_card <= 10:
	card_name = my_rand_card
elif my_rand_card == 11:
	card_name = 'Jack'
elif my_rand_card == 12:
	card_name = 'Queen'
else:
	card_name = 'King'

if my_rand_suit == 1:
	suit_name = 'Spades'
elif my_rand_suit == 2:
	suit_name = 'Clubs'
elif my_rand_suit == 3:
	suit_name = 'Diamonds'
else:
	suit_name = 'Hearts'

print(f'Your card is the {card_name} of {suit_name}')


# Just to make the point, I could have also written
# it this way because (critically) only the first
# matching branch of the if-elif-elif... tree is executed
if my_rand_suit >= 4:
	suit_name = 'Hearts'
elif my_rand_suit >= 3:
	# see how even if the value is 4,
	# and is greater-than-or-equal to 3,
	# this branch wouldn't be executed
	# because it hits the greater-than-or-equal
	# to 4 branch first?
	suit_name = 'Diamonds'
elif my_rand_suit >= 2:
	suit_name = 'Clubs'
else:
	# must be 1
	suit_name = 'Spades'
