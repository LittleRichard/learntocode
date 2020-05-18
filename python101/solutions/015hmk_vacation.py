# this is a little silly, but will reinforce everything
# required to start using internet-based APIs

# create a dictionary that will represent our checked bag
checked_bag = {
    'sets of clothes': 5,
    'passport': 1,
    'toiletries bag': {
        'toothbrush': 1,
        'toothpaste': 1,
        'conditioner': 1,
    },
    'books': [
        'for whom the bell tolls',
        'harry potter and the goblet of fire',
        'captain underpants anthology',
    ],
}

# create a dictionary that will represent our carry-on
carry_on_bag = {
    'cash': 250.00,
    'books': [
        'harry potter and the prisoner of azkaban',
    ],
    'plane ticket': 1,
    'pizzeria pretzel combos': 3,
    'bottled water': 1,
}

import random
import pprint 
## TODO YOUR CODE BELOW

# DON'T: any functions for this script
# DO: use pprint library to 'pretty print' your dictionaries
# as you work on each step to debug! look up pprint usage on the internet

# 0. if you don't have a passport... uh oh.
if 'passport' not in checked_bag and 'passport' not in carry_on_bag:
    exit('cancelled trip, missing passport')

# 1. Don't forget to bring a towel! check your checked bag to see if you have 
# one, and put one in if you don't.
if 'towel' not in checked_bag:
    checked_bag['towel'] = 1

# 2a. check in for your flight, do you have a passport?
# 2b. should probably put your passport in your carry-on...
if 'passport' in checked_bag:
    passport_val = checked_bag.pop('passport')
    carry_on_bag['passport'] = passport_val

# 3. board the plane (spend a ticket)
carry_on_bag['plane ticket'] -= 1

# 4. eat a bag of combos and drink half your water.
carry_on_bag['pizzeria pretzel combos'] -= 1
carry_on_bag['bottled water'] -= 0.5

# 5a. steal 5 nips of Jack Daniels while the flight attendant isn't looking,
# drink two and put the other in your carry-on
# 5b. tip the flight attendant generously for lacking vigilance
stolen_nips = 5
stolen_nips -= 2
carry_on_bag['Jack Daniels nips'] = stolen_nips
carry_on_bag['cash'] -= 25

# 6. pay up front for your hotel ($124.99)
if carry_on_bag['cash'] < 124.99:
    exit('uh oh, ran out of cash...')

carry_on_bag['cash'] -= 124.99

# 7. hit the ATM to replenish your cash
carry_on_bag['cash'] += 100

# 8a. apply a bottle of sunscreen
if 'sunscreen' not in carry_on_bag and 'sunscreen' not in checked_bag:
    print('burn baby burn')
elif 'sunscreen' in checked_bag:
    checked_bag['sunscreen'] -= 1
else:
    carry_on_bag['sunscreen'] -= 1

# 8b. take your towel and a book to the beach
towel = checked_bag.pop('towel')
book = checked_bag['books'].pop()

# hit the beach

# 8c. put your towel and book back
checked_bag['towel'] = towel
checked_bag['books'].append(book)

# 9. eat the local cuisine, take a 50-50 chance of feeling too terrible to
# drink the rest of the Jack Daniels.
if random.random() >= .5: # random float between 0 and 1
    feel_terrible = True
    print('ruh roh, montezumas revenge')
else:
    feel_terrible = False

if not feel_terrible:
    carry_on_bag['Jack Daniels nips'] = 0

# 10. wake up, brush your teeth with the Jack Daniels if you have
# any in your carry-on or checked bag.  If not, use all your toothpaste.
if 'Jack Daniels nips' in carry_on_bag and carry_on_bag['Jack Daniels nips'] > 0:
    carry_on_bag['Jack Daniels nips'] -= 1
else:
    print('Toothpaste is boring')
    checked_bag['toiletries bag']['toothpaste'] -= 1

# 11. almost done with the carry-on book, take a random one out of
# your checked-bag and put it in your carry on.
random_book_idx = random.randint(0, len(checked_bag['books']) - 1)
random_book = checked_bag['books'].pop(random_book_idx)
carry_on_bag['books'].append(random_book)

# ...you can continue to vacation if you like, or
# 12a. print a new ticket and put it in your carry-on
carry_on_bag['plane ticket'] +=1
# 12b. go to the airport, check your passport
if 'passport' not in checked_bag and 'passport' not in carry_on_bag:
    exit('Missing passport, trapped in paradise')

# 12c. spend your ticket to board the plane
carry_on_bag['plane ticket'] -= 1

# 12d: eat your remaining combos on the flight
carry_on_bag['pizzeria pretzel combos'] -= (
    carry_on_bag['pizzeria pretzel combos'])

# 12e. spend cash on a taxi to get home
carry_on_bag['cash'] -= 34.25

if feel_terrible:
    print('im never leaving home again')
else:
    print('what a great vacation!\n')

print('ended with a checked bag holding')
pprint.pprint(checked_bag)
print('')

print('ended with a carry-on holding')
pprint.pprint(carry_on_bag)
print('')