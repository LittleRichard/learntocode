import pprint

print("""
The dictionary is the most flexible and useful
of all fundamental datastructures. It is
a key-value store, so that instead of using
a 0-based index to access an element you can
use ANY (non-hashed) data to access an element.

Benefits: power, control, convenience
Tradeoffs: consume more memory
""")

# lets map store inventory to price
# we use curly braches to denote the dictionary,
# and `KEY: VALUE,` to denote each key-val pair
my_hardware_store = {
    'Hammer': 8.99,
    'Box of nails': 2.49,
    'Screwdriver': 4.99,
}

# access a value using square brackets and the key
hammer_cost = my_hardware_store['Hammer']
print(f'hammers cost {hammer_cost}')

# a dict can only have one instance of each key
# any 'hashable' datatype can be a key!
my_weird_dict = {
    'key1': 1,
    'key1': 2, # same key! overrides the 'key1': 1
    'key1': 3, # same key! overrides the 'key1': 2
    'key1': 4, # same key! overrides the 'key1': 3
    'key1': 5, # same key! overrides the 'key1': 4
    10: 55,
    (1, 2, 3): 'keyed by a tuple',
    'dict inside dict': {
        'inner dict key': 'inner dict value'
    }
}
print(f'dictionaries look like crap in printed output')
print(f'{my_weird_dict}')
print('')

# we can use the 'pretty print' builtin library to help use
import pprint
pprint.pprint(my_weird_dict)
print('')


# how to iterate over a dict
# some_dict_variable.keys() -> iterates over the keys
list_of_keys = list(my_hardware_store.keys())
print(f'Keys list: {list_of_keys}')
# some_dict_variable.itervalues() -> iterates over the values
list_of_values = list(my_hardware_store.values())
print(f'Values list: {list_of_values}')
# some_dict_variable.iteritems() -> iterates over tuples of (key, value)
list_of_items = list(my_hardware_store.items())
print(f'Items list: {list_of_items}')
print('')
# dicts are NOT an ordered datatype!!!!!!!
# you can order their keys for iteration if you want,
# but using them as an iterable can result in
# a different order every time.
print("""Important! Dictionary keys are not iterated 
over in a predicatable order, just like with sets.""")
# that said, the order is usually (not always!!!) consistent
# within execution of a script

# let's make a function since we're going to do this a lot
def print_store_inventory(store_dict):
    # you can use len to count number of keys
    num_items = len(my_hardware_store)
    
    print(f'Hardware store has {num_items} different things')
    for key, value in store_dict.items():
        print(f'A {key}, which costs {value}')
    print('')

print_store_inventory(my_hardware_store)

# you can update dictionaries like a list; adding
# a new key/value looks just like an update!
my_hardware_store['Sledgehammer'] = 29.99
print_store_inventory(my_hardware_store)

# if the key is present, updates the value
my_hardware_store['Hammer'] = 10.99 # hammers got more expensive
print_store_inventory(my_hardware_store)

# define a blank dictionary
my_dict = {}
# or use the equivalent statement
my_dict = dict()
print('made a new dict')

# let's set a new key into our empty dict
my_dict['this is a key'] = 'this is a value'
my_dict['another key'] = 'the dict gets bigger'
my_dict['dict size'] = 'now this is a decent sized dict'

# use the pretty print library, pprint
print('')
pprint.pprint(my_dict)
print('')

extracted_value = my_dict['this is a key']
print(extracted_value)
print('')

# you can remove values by 'popping' them out
for idx in range(3): # iterate three times
    # containement checks (the `in`) will only
    # check the KEYS of a dictionary, not the values.
    if 'this is a key' in my_dict:
        popped_value = my_dict.pop('this is a key')
        print(f'popped value: {popped_value}')
    else:
        print('did nothing')

# for-loop should print that it popped a value,
# then did nothing for all further iterations.
print(my_dict)

print("""
You will get an error if you try to access a key that
is not present:

>>> my_dict['this key is not present']
would result in:
>>> KeyError: 'this key is not present'
""")
# nonexistent_value = my_dict[100] # comment this line out to execute code after it
# Traceback (most recent call last):
#   File "016dictionaries.py", line 54, in <module>
#     print(m) # ERROR
# KeyError: 'this key is not present'

# the way around this is to use the .get() function
might_be_present_value = my_dict.get(100)
# if the key is present, might_be_present_value will hold the value
# if not, it will hold None
print(f'.get(100): {might_be_present_value}')

# None is a special value in python, like True and False
# it is generally used to mean the absence of a value,
# and is a great initialization value for variables
# that you will fill in while looping
print(f'type(None): {type(None)}, None: {None}')

print("""
Dicts are very powerful, so make sure you play
with them to get firm grip on how they work.

Like sets, there are lots of other things you can do
with them; check the python docs.
https://docs.python.org/3/library/stdtypes.html#dict
""")