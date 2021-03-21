import hashlib

print('Bits & Bytes are sometimes important (and cool!)')

# a hash is the result of a math equation that
# takes an arbitrary amount of infomation and
# reduces it to an integer. there are a few 
# different types of hashes, but we're going 
# to focus on the 'avalanche hash'

# the b preceding the string indicates the encoding;
# bits and bytes but suffice it to say it's just to
# make the hash library happy.
my_string = b"""
This string could be of any length, so
this is just demonstration"""

# hashlib is a builtin library to work with hashes
# sha256 and it's siblings are used in lots of
# the encryption layers of the internet

# create a hash 'object' that we'll add data
# to as we go.
hash_obj = hashlib.sha256()

# add our string to the hash obj so it knows
# what it will be processing.
hash_obj.update(my_string)

# trigger the computation of the hash and
# print the result
hashed_output = hash_obj.hexdigest()
print(f'hashed output:  {hashed_output}')

# if i hash the same data again, i get the same result
hashed_output2 = hash_obj.hexdigest()
print(f'hashed_output2: {hashed_output2}')

# but if i make any tiny change to the input,
# it results in a huge change in the output
# this is the 'avalanche'
my_string += b"a"
new_hash_obj = hashlib.sha256()
new_hash_obj.update(my_string)
hashed_new = new_hash_obj.hexdigest()
print(f'hashed_new:     {hashed_new}')

# computation of hashes is relatively fast, and the
# avalanche property is fundamental to our next
# data structure functioning correctly.

print("""
A 'hash collision' is when two inputs hash
to the same output. In modern hash algorithms,
which use hundreds of bits of complexity, the
likelihood of this occurring is on the order
of choosing the same atom in the universe twice.
""")