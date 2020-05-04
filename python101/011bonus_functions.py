print('as a bonus, here is a richer example.')

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

    # this syntax is new, but using parentheses around strings
    # on different lines has the result of smashing them together.
    dinner_string = (
        f"I'm making {main_course} with {side_dish} for "
        f"{num_diners_str}, and {dessert} for dessert!")
    
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

# note that this styles the code inside parentheses to keep
# it from being too long to fit on screen. python doesn't care.
my_dinner = get_dinner(
    'Green Eggs', 
    'Ham', 
    100, 
    dessert='Sneetches', 
    print_constant=True)

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
