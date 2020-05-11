
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

# 0. if you don't have any of the following items packed, add it.
# Don't worry about iterating through the dictionary to search, 
# assume you know where everything should be:
# - passport
# - plane ticket
# - cash
# - shampoo

# the `exit()` function ends your script immediately and prints
# whatever message you provide on the way out.
exit(f'cancelled trip, missing: {"TODO add checks for stuff"}')

# 1. Don't forget to bring a towel! check your checked bag to see if you have 
# one, and put one in if you don't.


# 2a. check in for your flight, do you have a passport?
# 2b. should probably put your passport in your carry-on...


# 3. board the plane (spend a ticket)


# 4. eat a bag of combos and drink half your water.


# 5a. steal 5 nips of Jack Daniels while the flight attendant isn't looking,
# drink two and put the other in your carry-on
# 5b. tip the flight attendant generously for lacking vigilance


# 6. pay up front for your hotel ($124.99)


# 7. hit the ATM to replenish your cash


# 8a. apply a bottle of sunscreen, 
# 8b. take your towel and a book to the beach
# 8c. put your towel and book back


# 9. eat the local cuisine, take a 50-50 chance of feeling too terrible to
# drink the rest of the Jack Daniels.


# 10. wake up, brush your teeth with the Jack Daniels if you have
# any in your carry-on or checked bag.  If not, use all your toothpaste.

# 11. almost done with the carry-on book, take a random one out of
# your checked-bag and put it in your carry on.

# ...you can continue to vacation if you like, or
# 12a. print a new ticket and put it in your carry-on
# 12b. go to the airport, check your passport
# 12c. spend your ticket to board the plane
# 12d: eat your remaining combos on the flight
# 12e. spend cash on a taxi to get home

print('what a great vacation!\n')

print('ended with a checked bag holding')
pprint.pprint(checked_bag)
print('')

print('ended with a carry-on holding')
pprint.pprint(carry_on_bag)
print('')
