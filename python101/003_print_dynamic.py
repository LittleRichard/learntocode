
print('This string is boring, it can only say one thing')

# dynamic insertion of values into strings is called 'string interpolation'

number_of_cows = 25
print('There are %d cows on my farm' % number_of_cows) # %d is for 'decimal'
# think of interpolation as having 2 parts:
## template string (has %s/%f/%d in it)
## interpolated values (the stuff after the %)

# this is a 'floating point' number, lot of complexity here but just know that it's different than an integer
cost_of_JBC = 1.39
print('A Junior Bacon Cheeseburger costs %f' % cost_of_JBC) # %f is for 'float'
# %f prints a bunch of decimal places by default, but
# you can specify a little bit more detail of how these are printed
print('A Junior Bacon Cheeseburger costs %.2f' % cost_of_JBC) # use 2 decimal points

# can also do this with strings using %s
my_base_string = 'My name is %s'
my_name = 'Anson'
# remember that variables are just placeholders for the data they hold
print(my_base_string % my_name)
# equivalent to: 'My name is %s' % 'Anson'
# this uses only variables! can you start to see the power this has to process data?

# Use multiple values
my_interpolated_string = '%s %d %f' % ('abc', 123, 456.789)
print(my_interpolated_string)

# when in doubt, go with %s because python has a default 'string' way of 
# printing anything
print('1 + 1 is %s' % 2.0)

# be careful though, it's easy to screw up interpolation
my_interpolated_string = '%s %d %s' % ('abc', 123)
# Traceback (most recent call last):
#   File "print_dynamic.py", line 30, in <module>
#     my_interpolated_string = '%s %d %s' % ('abc', 123)
# TypeError: not enough arguments for format string

# confirm you can do this by:
## create a variable holding the number of toes you have
num_toes = 10
## print a statement of how many toes you have
print('i have %d toes' % num_toes)
print('i have %s toes' % num_toes) # %s handles most things well
## create a variable holding a template string (one that contains %s, %d, or %f as necessary)
template_string = 'my favorite foods are: %s, %s, and %s'
## print a statement of your three favorite foods, in order
print(template_string % ('macaroni and cheese', 'PANCAKES', 'pizza'))
