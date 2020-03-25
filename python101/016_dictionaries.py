import pprint

# a dictionary is a key-value datatype
# the key can be (just about) anything
# the value can be anything

# lets map store inventory to price
my_hardware_store = {
    # KEY: VALUE,
    'Hammer': 8.99,
    'Screwdriver': 4.99,
    'Box of nails': 2.49,
}
assert isinstance(my_hardware_store, dict)

# access a value using square brackets and the key
hammer_cost = my_hardware_store['Hammer']
print('hammers cost %s' % hammer_cost)

# sometimes you'll see a dictionary referred
# to as a hash map.  Dictionaries use an 'avalanche hash'
# to handle the keys.  An avalanche hashing algorithm
# will take a single-bit change in the input and turn it into
# a huge change in the output.  This is how we can
# guarantee that dictionary keys don't collide, even
# though we can (practically speaking) have an infinite number of them.

# a dict can only have one instance of each key
# any 'hashable' datatype can be a key!
my_weird_dict = {
    'key1': 1,
    'key1': 2, # same key! overrides the 'key1': 1
    10: 55,
    (1, 2, 3): 'keyed by a tuple',
    'dict inside dict': {
        'inner dict key': 'inner dict value'
    }
}
print('dictionaries look like crap in printed output: %s' % my_weird_dict)
print('')
pprint.pprint(my_weird_dict)
print('')


# how to iterate over a dict
# some_dict_variable.iterkeys() -> iterates over the keys
list_of_keys = list(my_hardware_store.iterkeys())
print('Keys list: %s' % list_of_keys)
# some_dict_variable.itervalues() -> iterates over the values
list_of_values = list(my_hardware_store.itervalues())
print('Values list: %s' % list_of_values)
# some_dict_variable.iteritems() -> iterates over tuples of (key, value)
list_of_items = list(my_hardware_store.iteritems())
print('Items list: %s' % list_of_items)
print('')
# dicts are NOT an ordered datatype!!!!!!!
# you can order their keys for iteration if you want,
# but using them as an iterable can result in
# a different order every time.
print('Important! Dictionary keys are not iterated over in a predicatable order')
# that said, the order is usually (not always!!!) consistent
# within execution of a script

def print_store_inventory(store_dict):
    print('At the hardware store you can find')
    for key, value in store_dict.iteritems():
        print('A %s, which costs %.2f' % (key, value))
    print('')

print_store_inventory(my_hardware_store)

# you can update dictionaries,
# note that this inserts if not present, and updates otherwise
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
my_dict['dict joke'] = 'now this is a decent sized dict'

# use the pretty print library, pprint
print('')
pprint.pprint(my_dict)
print('')

extracted_value = my_dict['this is a key']
print(extracted_value)
print('')

# delete a key/value
for idx in xrange(3): # iterate three times
    if 'this is a key' in my_dict:
        popped_value = my_dict.pop('this is a key')
        print('popped value: %s' % popped_value)
    else:
        print('did nothing')
# for-loop should print that it popped a value,
# then did nothing for all further iterations.
print(my_dict)
print('')

print('the next line will fail')
# nonexistent_value = my_dict[100] # comment this line out to execute code after it
# Traceback (most recent call last):
#   File "016dictionaries.py", line 54, in <module>
#     print(my_dict['this key is not present']) # ERROR
# KeyError: 'this key is not present'

# the way around this is to use the .get() function
might_be_present_value = my_dict.get(100)
# if the key is present, might_be_present_value will hold the value
# if not, it will hold None
print(might_be_present_value)

# None is a special value in python, like True and False
# it is generally used to mean the absence of a value,
# and is a great initialization value for variables
# that you will fill in while looping