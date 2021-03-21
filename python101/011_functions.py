
# we've been using built in functions a little so far
print('this string is an argument to the print function')
my_tuple = tuple(range(3)) # tuple() and xrange(), both functions
my_len = len(my_tuple) # len is also a function

# but there's a lot of power in being able to write our own.
# imagine if you had to write the same code over and over
# every time you wanted to create a tuple...

# functions will help you BOTH:
## organize your code to make it understandable (name functions well!)
## save lots of time by re-using code that you'll need over and over.

# `def` is the python keyword that declares a function
def my_function():
    # a simple function, accepts no arguments
    # prints and returns a value
    print('in my_function!')
    return 55

# the returned value can be assigned to a variable
my_return_val = my_function()
print(f'function gave me {my_return_val}')
# you don't HAVE to do anything with the return,
# python is happy to drop it on the floor
my_function()
print('')

# you can provide 'positional' arguments to a function
# by separating them with commas.  The variable name
# in the declaration of the function will hold the
# values passed into the function for each position.
def add_them_plus_one(input1, input2):
    return input1 + input2 + 1

# now for the rest of this script, i can perform
# this action anytime i want without re-writing 
# the code!
sum_val = add_them_plus_one(39, 27)
print(f'got back {sum_val}')

# what happens if we give the function a non-integer?
print("""
this next line would cause an error:

add_them_plus_one(34, 'not an integer')
""")
print('')

# our function wasn't designed to work with integers.
# python doesn't have type-checking built in, so you need
# to be careful! there are ways to enforce a type check,
# but they're optional.  i like to use them to save myself
# from myself, but choose your own adventure.

# in addition to positional arguments, you can use 
# keyword arguments, AKA 'kwargs', and can be provided 
# as shown below, the ones like:
#    func_name(variable_name='default value')
# these are optional arguments, and if not passed will
# use the value defined in the function declaration.
def using_keyword_args(my_tuple, index_to_grab=0, check_length=False):
    if check_length:
        if len(my_tuple) == 0 or index_to_grab >= len(my_tuple):
            return 'invalid index'

    return my_tuple[index_to_grab]

# you can provide keyword arguments in any order!
# you CAN provide a keyword argument positionally, but 
# do not do this or you'll confuse yourself and others!

print(f'you might recognize kwargs from the `sorted()` function')
print(f'reversed/sorted: {sorted((1,2,3), reverse=True)}')

tuple_for_func = (3,4,5)

# provide no kwargs
result_val = using_keyword_args(tuple_for_func)
print(f'no kwarg: {result_val}')

# provide one kwarg
result_val = using_keyword_args(tuple_for_func, index_to_grab=2)
print(f'just index_to_grab: {result_val}')

# provide the other kwarg
result_val = using_keyword_args(tuple(), check_length=True)
print(f'just check_length: {result_val}')

# function arguments will often make the line too long, start
# practicing how to 'style' your code to look better without
# breaking syntax.  

# both in 'correct' order
result_val = using_keyword_args(
    tuple_for_func, index_to_grab=1, check_length=True)
print(f'both kwarg in order: {result_val}')

# both in wrong order
result_val = using_keyword_args(
    tuple_for_func, check_length=True, index_to_grab=1)
print(f'both kwarg in different order: {result_val}')

# use keyword arguments when you have a very common usage of 
# the function without the extra value, but still want to have
# the power to change it sometimes.
# 'debug mode' is a great example: debug_mode=False


print('')

# 'scope' is the technical term for which variables
# a function can see.
# this gets much more complicated stuff with object-oriented code

MY_CONSTANT = 'my constant string'
print(MY_CONSTANT)

def demo_scope(): # no args necessary
    # why?!?! because MY_CONSTANT doesn't exist INSIDE
    # this function.
    print("""
        the next line would cause an error: 

        print(f'in func, constant is {MY_CONSTANT}')  
        """)

    MY_CONSTANT = 3456
    print(f'in func, set constant to {MY_CONSTANT}')

# YOU HAVE TO be careful of 'variable scope', because
# it can get really confusing to debug.
print(f'outside function before: {MY_CONSTANT}')

demo_scope()

# notice how our constant never changes? that's because
# the outer-scoped constant wasn't edited, one that
# just happened to share a name was created inside the function.
print(f'outside function after: {MY_CONSTANT}')

print("""
Variable scope issues can be confusing and hard to debug,
the best solution is prevention:
1. don't use the same variable names inside and outside
   scripts (unless it's an `x` and clearly transient)
2. think of your functions as little sealed packets; if
   the info isn't passed in, the function doesn't know it.
""")

# IN CONCLUSION, it's generally a good idea to create 
# functions for things that are:
# 1) Re-used.  Repetitive code becomes a nightmare over time,
#    because changes must be applied to each copy-pasted block of code.
#    If it's in a function you only have to fix it in one place.
#    If it's used all the time, even 2-3 lines can make sense to put in
#    a function.  If the same code is used twice, my threshold is 
#    closer to 10-15 lines.
# 2) Longer than 25-50 lines and looks complicated.  Just hide it
#    in a function to make your code more readable.  Well-named functions 
#    will help your program read like steps in a recipe, 
#    so you can put a bunch of variables that do something complicated 
#    behind the curtain and let you use them with just one line.

# Finding the balance just takes time and practice, and is
# open to intepretation.  Over time you'll start to spot patterns
# in code that are repetitive but have one value that changes; these
# are ripe for function-izing!
