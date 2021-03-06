import random # import is how you tell python that you want to use a library in a script

# 'if' and 'True' are python KEYWORDs, and should NEVER EVER be used as a variable
if True:
	print('Obviously...')

# False is a python KEYWORD, and should NEVER EVER be used as a variable
if False:
	print('This will never be printed.')

print('') # print a blank line

my_rand_int = random.randint(1, 2) # returns a value: 1 or 2
print(f'my random int is {my_rand_int}')

# essentially: if X, do Y
if my_rand_int == 1: # the '==' operator returns True if the two elements are equal, False otherwise
	print('is 1')

if my_rand_int != 1: # the '!=' operator returns 'True' if the two elements are equal, False otherwise
	print('was 2')

# simulate a coin flip, which has two obvious outcomes
if my_rand_int == 1:
	print('Heads')
else: # 'else' is a python KEYWORD, and should NEVER EVER be used as a variable
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
	print('Landed on the edge, %s was zero!' % bigger_rand_int)

# each indented block MUST have at least one statement! If you want to 
# represent a case in your if-elif-elif... tree
# you should use the 'pass' python keyword.  
# python interprets the 'pass' to mean 'do nothing'
if -25 < 0:
	pass

print('') # print a blank line


# <TRY IT OUT>
## grab a random integer between 1 and 5


## write an if-tree that will:
### print some text if the integer is 1 or 2
### print some text if the integer is 3 or 4
### print something else if it's 5

