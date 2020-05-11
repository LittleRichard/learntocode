

# a set is a hashed datatype, which means it
# relies on hashing values to determine whether
# or not they are present in the set.
my_set = set()

# each element in the set is hashed, so you can't
# have duplicates!!! same value, same hash.
my_set.add('abc')
print(f'my_set 1: {my_set}')
my_set.add('def')
print(f'my_set 2: {my_set}')
# adding abc again won't have any effect,
# because hash('abc') == a value already in the
# set!!!
my_set.add('abc')
print(f'my_set 3: {my_set}')

print("""
Because a set tracks all it's contents using
hashes, lookups happen by computing the hash
and comparing hashes, not checking each
value for equality! This is SO much faster
""")

integers_set = set()
integers_set.add(11)
integers_set.add(22)
integers_set.add(33)
integers_set.add(-44)
integers_set.add(55)
if 33 in integers_set:
    print('33 is in the set!')

print("""
The tradeoff here is that sets are not
ordered, so while you can iterate over them,
the elements won't (necessarily) come out
in the order you put them in
""")

for x in integers_set:
    print(f'int set has: {x}')

# some more set operations
final_set = set(range(5))
print(f'final_set 1: {final_set}')
final_set.remove(3)  # error if 3 not present
print(f'removed 3: {final_set}')
final_set.discard(100)  # totally cool with 100 not present

final_set.clear()
print(f'cleared set {final_set}')

print("""
There are lots of other things you can do with
sets around comparing them for union/disjoint, shared
elements, etc.
https://docs.python.org/3/library/stdtypes.html#set
""")