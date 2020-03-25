import random # import is how you tell python that you want to use a library in a script

if True: # 'if' and 'True' are python KEYWORDs, and should NEVER EVER be used as a variable
	print('Obviously...')

if False: # False is a python KEYWORD, and should NEVER EVER be used as a variable
	print('This will never be printed.')

print('') # print a blank line

my_rand_int = random.randint(1, 2) # returns a value: 0 or 1
print(my_rand_int)

# if one thing, do another
if my_rand_int == 1: # the '==' operator returns 'True' if the two elements are equal, False otherwise
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
BIG_RAND_INT_MAX = 1000000
bigger_rand_int = random.randint(0, BIG_RAND_INT_MAX) 
print(bigger_rand_int)

# X < value < Y is a special operator equivalent to (X < value) and (value < Y)
if 40 < bigger_rand_int < 80000:
    print('between 40 and 80')

if bigger_rand_int >= (BIG_RAND_INT_MAX / 2): 
    print('Heads')
elif bigger_rand_int > 0:
    # 'elif' is a python KEYWORD, and should NEVER EVER be used as a variable
    print('Tails')
else:
	print('Landed on the edge, %s was zero!' % bigger_rand_int)

# each indented block MUST have at least one statement! If you want to represent a case in your if-elif-elif... tree
# you should use the 'pass' python keyword.  python interprets the 'pass' to mean 'do nothing'
if -25 < 0:
	pass

print('') # print a blank line

# confirm by:
## grab a random integer between 1 and 5
final_random_int = random.randint(1, 5)
## write an if-tree that will:
### print some text if the integer is 1 or 2
### print some text if the integer is 3 or 4
### print something else if it's 5
if 1 <= final_random_int <= 2:
    print('its a 1 or 2! %s' % final_random_int)
elif 3 <= final_random_int <= 4:
    print('its a 3 or 4! %s' % final_random_int)
else:
    print('its a 5! %s' % final_random_int)