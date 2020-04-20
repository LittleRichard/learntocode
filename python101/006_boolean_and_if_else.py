import random # import is how you tell python that you want to use a library in a script

# 'True' is a python KEYWORD, and should NEVER EVER be used as a variable
# note how the code editor uses a different color for True than print
print(f'True is {True}, duh')

# True is a 'boolean' type, in addition to the
# 'int' (integer) and 'str' (string) types we know. 
# We can use python's built-in function 'type' to inspect them
print(type(1))
print(type('1'))
print(type(True))

my_rand_int = random.randint(1, 2) # returns a value: 1 or 2
print(f'my random int is {my_rand_int}')

# IMPORTANT: we're about to start indenting code, which means something
# to python syntactically.  Set your code editor to use 4 spaces as
# an indent!!!!!!!!
# Some languages use {} or other syntax to denote blocks of code, but
# python uses indentation.

# 'if' is part of python syntax.
# the indented bit is only executed when the 'condition' following it
# evaluates to True.  
# essentially: if X, do Y
if my_rand_int == 1:
    # the '==' operator returns True if the two elements are equal, 
    # and returns False otherwise
    print('is 1')

if my_rand_int != 1:
    # the '!=' operator returns True if the two elements are NOT equal, 
    # and returns False otherwise
    print('was 2')

# False is a python KEYWORD, and should NEVER EVER be used as a variable
if True:
	print('turns out True is still true')

# False is a python KEYWORD, and should NEVER EVER be used as a variable
if False:
	print('This will never be printed.')

print('') # print a blank line

# simulate a coin flip, which has two obvious outcomes
if my_rand_int == 1:
	print('Heads')
else: 
    # 'else' is a python KEYWORD, and should 
    # NEVER EVER be used as a variable
	print('Tails')

print('') # print a blank line

# not quiiiite accurate to the real-world act, let's add a third case
BIG_RAND_INT_MAX = 200000
bigger_rand_int = random.randint(0, BIG_RAND_INT_MAX) 
print(f'random integer with max {BIG_RAND_INT_MAX}: {bigger_rand_int}')

# value < Y is a special operator equivalent to (X < value) and (value < Y)
if bigger_rand_int < 80000:
    print('less than 80000')

if bigger_rand_int >= (BIG_RAND_INT_MAX / 2): 
    print('Heads')
elif bigger_rand_int > 0:
    # 'elif' is a python KEYWORD, and should NEVER EVER be used as a variable
    print('Tails')
else:
	# note that our elif used >, NOT >=
	print(f'Landed on the edge, {bigger_rand_int} == 0')

# each indented block MUST have at least one statement! If you want to 
# represent a case in your if-elif-elif... tree
# you should use the 'pass' python keyword.  
# python interprets the 'pass' to mean 'do nothing'
if -25 < 0:
	# using pass is convenient if your if-elif-elif tree
	# wants to check for a case but skip it.  you typically
	# won't need it, but it's handy just in case.
	pass

print('') # print a blank line

# this is a good opportunity to demostrate that integers and strings
# are not equivalent, even if they seem to be!!!
if 123 != '123':
	print("always remember: 123 != '123'")

# <TRY IT OUT>
## grab a random integer between 1 and 5, inclusive

## write an if-tree that will:
### print some text if the integer is 1 or 2
### print some text if the integer is 3 or 4
### print something else if it's 5
