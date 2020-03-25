
# here, i'll show you why constants should be ALL_CAPS
MY_CONSTANT = 'my constant string'

# we've been using built in functions a little so far
print('this string is an argument to the print function')
my_tuple = tuple(xrange(3)) # tuple() and xrange(), both functions
my_len = len(my_tuple) # len is also a function

# but there's a lot of power in being able to write our own.
# imagine if you had to write the same code over and over
# every time you wanted to create a tuple...

# functions will help you BOTH:
## organize your code to make it understandable (name functions well!)
## save lots of time by re-using code that you'll need over and over.

def my_function():
    # a simple function, accepts no arguments
    # prints and returns a value
    print('in my first function!')
    return 55

my_return_val = my_function()
print('function gave me %s' % my_return_val)
# you don't HAVE to do anything with the return,
# python is happy to drop it on the floor
my_function()
print('')

def add_them_plus_one(input1, input2):
    return input1 + input2 + 1

sum_val = add_them_plus_one(39, 27)
print('got back %s' % sum_val)

# what happens if we give the function a non-integer?
print('the next line will cause an error 1')
# add_them_plus_one(34, 'not an integer')

print('')

# our function wasn't designed to work with integers.
# python doesn't have type-checking built in, so we use 
# the 'assert' statement to INTENTIONALLY cause an error.

# assert (a boolean logic statement), 'prints if failed'
assert True, 'this will never print because it always succeeds'
print('the next line will cause an error 2')
# assert False, 'asserted false, which always prints this'

print('')

def func_with_type_checks(input1, input2, input3, input4):
    # isinstance is a function that returns True
    # if the first value is of the type provided in the second value
    assert isinstance(input1, int), type(input1)
    assert isinstance(input2, float), type(input2)
    assert isinstance(input3, str), type(input3)
    assert isinstance(input4, tuple), type(input4)

    assert input1 >= 0 # you don't NEED to provide something to display
    assert input2 != 3.14159
    assert len(input3) < 10
    assert len(input4) > 0
    assert input4[0] == 4, input4

    print('passed assertions with %s %s %s %s' % (input1, input2, input3, input4))

    # note that there is not a return statement, it can be omittied
    # and the function will return a python built-in similar to 
    # True and False called None.

# assertions are a stylistic choice, many people ignore them.
# but i've found that it helps me find bugs before they're
# too deeply rooted to yank out.
func_with_type_checks(1, 2.0, '3', (4,5,6))
print('the next lines will all cause an error 3')
# func_with_type_checks(1, 2.0, 3, (4,5,6)) # easy mistake...
func_with_type_checks(1, 2.0, '3', (3,5,6)) # easy mistake...
# func_with_type_checks(-1, 2.0, '3', (4,5,6)) # easy mistake...

print('')

# keyword arguments are provided as shown below, the ones like:
# variable_name='default value'
def using_keyword_args(my_tuple, index_to_grab=0, check_length=False):
    # the value in the function's signature is the value
    # that the function will use if no other value is provided
    assert isinstance(my_tuple, tuple)
    assert isinstance(index_to_grab, int)
    assert isinstance(check_length, bool) # bool for boolean

    if check_length:
        if len(my_tuple) == 0 or index_to_grab >= len(my_tuple):
            return 'invalid index'

    return my_tuple[index_to_grab]

tuple_for_func = (3,4,5)
result_val = using_keyword_args(tuple_for_func)
print(result_val)

result_val = using_keyword_args(tuple_for_func, index_to_grab=2)
print(result_val)

result_val = using_keyword_args(tuple(), check_length=True)
print(result_val)

# use keyword arguments when you have a very common usage of 
# the function without the extra value, but still want to have
# the power to change it sometimes.
# 'debug mode' is a great example: debug_mode=False


print('')

# 'scope' is the technical term for which variables
# a function can see.
# this gets much more complicated stuff with object-oriented code
print(MY_CONSTANT) # remember this from the top?

def demo_scope(): # no args necessary
    print('the next lines will cause an error 4')
    # print('in func, constant is %s' % MY_CONSTANT)
    # why?!?! because MY_CONSTANT doesn't exist INSIDE
    # this function.
    MY_CONSTANT = 3456
    print('in func, set constant to %s' % MY_CONSTANT)

# YOU HAVE TO be careful of 'variable scope', because
# it can get really confusing to debug.
print('outside function before: %s' % MY_CONSTANT)

my_dinner = demo_scope()

# notice how our constant never changes? that's because
# the outer-scoped constant wasn't edited, one that
# just happened to share a name was created inside the function.
print('outside function after: %s' % MY_CONSTANT)


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
# open to intepretation.



SHOW_COMPLETE_EXAMPLE = False
if not SHOW_COMPLETE_EXAMPLE:
    exit()

# i re-did this script to make it simpler,
# but the function below and the example usage
# of it demostrates everything you'll need to know

# functions are defined using the 'def' keyword
def get_dinner(main_course, side_dish, num_diners, dessert='Stale Oreos', print_constant=False):
    # the first 3 variables: main_course, side_dish, num_diners
    # are called positional arguments.  A value must be 
    # provided or BOOM

    # assertions are an EXTREMELY useful tool in python.  It blows
    # up and fails out of the program (just like it does for a syntax error
    # or if you didn't declare a variable before using it) if the assertion isn't true.
    
    # ALWAYS PUT ALL POSITIONAL ARGUMENTS FIRST, followed by kwargs.
    # you don't have to, but if you do you'll end up in hell.

    # the last two: dessert and print_constant
    # are keyword arguments.  You can have as many as you want.
    # They are ALL optional, and would be used as:
    #get_dinner('steak', 'potatoes', 4, dessert='Twinkies')
    # if it isn't provided, the value in that variable is 
    # the default defined above as:
    # ..., dessert='A dessert'):

    # Functions are where assertions shine, because they help us make sure
    # that the stuff we're giving our function is what we expect

    # the 'isinstance' builtin function returns True if the first value's 'type'
    # matches the 2nd value
    assert isinstance(main_course, str), main_course # asserts, if BOOM prints main_course
    assert isinstance(side_dish, str), side_dish 
    assert isinstance(num_diners, int), num_diners
    assert num_diners >= 1 # we can't serve dinner for just one...
    assert isinstance(dessert, str), dessert
    assert isinstance(print_constant, bool) # better be a boolean

    if num_diners == 2:
        num_diners_str = 'just the two of us ;)'
    else: 
        num_diners_str = '2'

    dinner_string = "I'm making %s with %s for %s, and %s for dessert!" % (
                                                                           main_course, 
                                                                           side_dish, 
                                                                           num_diners_str,
                                                                           dessert,
                                                                           )
    
    # the 'return' keyword does exactly that, it returns
    # the value back up to whatever code called the function.
    return dinner_string
    # the return keyword is optional, and the return will
    # be a python-defined constant called None.
    # you're also free to ignore returned values when you
    # call a function, python will just ignore them

    # we're technically still scoped inside the function, but no
    # more code is executed after a return statement
    assert False, "This line never executes"

# end get_dinner

my_dinner = get_dinner('Green Eggs', 'Ham', 100, dessert='Sneetches', print_constant=True)

print(my_dinner)
print('')

print('the next line will throw an error')
# my_dinner = get_dinner('green eggs', 'ham', 'Sam I Am') 
# and then see
#AssertionError
# it blows up because the 3rd argument is not an integer!
# An example stack trace, the bottom most is the actual line
# that failed. Above it, you can see the line that called
# the function that failed; repeat until you get to the main script.
# Stack Trace:
# Traceback (most recent call last):
#   File "012_functions.py", line 234, in <module>
#     my_dinner = get_dinner('green eggs', 'ham', 'Sam I Am')
#   File "012_functions.py", line 197, in get_dinner
#     assert isinstance(num_diners, int), num_diners
# AssertionError: Sam I Am



the_worst_date_ever_dinner = get_dinner('Mayonnaise', 'Pork Rinds', 2)
print(the_worst_date_ever_dinner)
print('')