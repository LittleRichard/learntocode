
print('This string is boring, it can only say one thing')

# this is an f-string, though we're not using its special properties yet.
print(f'notice how in the code the quote defining this string is preceded by "f"?')

# dynamic insertion of values into strings is called 'string interpolation'
number_of_cows = 25
print(f'There are {number_of_cows} cows on my farm')
# when interpolating you'll have the following:
# # base string: the parts that don't change
# # interpolated value(s): the variables to insert into the base string
# # formatting code: special syntax (like the '{' and '}' above, more in a few lines)

# can also do this with strings:
my_name = 'Abraham Lincoln'
my_interpolated_string = f'My name is {my_name}'
print(my_interpolated_string)

# this is a 'floating point' number, lots of bits & bytes
# to how non-integers work but a 'float' is just what
# the computer calls a number with decimal places.
cost_of_JBC = 1.99  # back in my day it was on the dollar menu
print(f'A Junior Bacon Cheeseburger costs {cost_of_JBC}')
# prints a bunch of decimal places by default, but
# you can specify a little bit more detail of how these are printed
# if you use a different syntax, NOT an f-string. it's a bit more complicated
# though so we'll skip it for now

# Use multiple values
menu_item = 'Chocolate Frosty'
multiple_values = f'{my_name} needs {number_of_cows} {menu_item}s for {cost_of_JBC}, pronto!'
print(multiple_values)

# NOTICE HOW:
# the previous string was almost entirely made of variables. Now if
# we change the variables, we can use THE SAME CODE to print anything
# of that format. This is where we start to become powerful

# confirm you can do this by:
# # create a variable holding the number of toes you have


# # print a statement of how many toes you have


# # declare 3 variables for your favorite foods


# # print a statement of your three favorite foods, in order

