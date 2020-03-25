# in python, anything following a '#' is a code comment and is ignored
# by python's interpreter.  code comments are notes for the next developer.

# this is a script.  it can be executed by python from the command line as:
# $ python3 my_awesome_script.py
# or in this case:
# $ python3 002_variables_ints_strings.py

# variables are a way for a programmer to name a 'thing' they want to re-use
# they can have any name using alphanumberic characters.
# # can't START with a number
# by convention, we use underscores where we'd use spaces

# we need a way to test our code, we'll use the 'print' function
print('hello world')  # you can print() just about anything
# !!!!!!!!!
# printing is your best friend while debugging
# !!!!!!!!!

# INTEGERS
# variables are a way of assigning a piece of information a label that
# you can reference later in the program
# define a variable: <variable name> = <value>
my_var1 = 111
print('my_var1')
print(my_var1)  # prints the contents of the variable 'my_var1', which is 111

# define another variable
my_var2 = 222
print('my_var2')
print(my_var2)  # prints the contents of the variable 'my_var2', which is 222

# variables can be overwritten to different value
third_var = 333
print('third_var')
print(third_var)  # prints third_var's current value, 333
print('third_var (the 2nd time)')
third_var = 444
print(third_var)  # prints third_var's current value, 444

# assign a variable into another!
my_var2 = my_var1
print('after my_var2 = my_var1')
print(my_var2)  # prints 111

# the original variable retains its value
print('my_var1 again')
print(my_var1)  # prints 111
# not always true for more advanced datatypes, but we'll get there

# STRINGS
# variables can also be text, called 'strings', and are defined one of 3 ways
print('the hello world we printed at the beginning was a string')
print('this is how you put a "new line" character in a string: \nsee?')

my_string1 = 'this is a string that says "this is a string"'  # note the use of ""
print(my_string1)

my_string2 = "a double quoted string won't care about single quotes"  # note the ' char in the middle
print(my_string2)

my_essay = """Triple quotes are very useful for when you
want to do
confusing things like: "My banana's pants have this symbol on them: '"'"
A triple-quote block prints exactly
as
you
type
it. 
# this is not a comment in a string!
"""
# keep it simple and just use the '' way, but know that you have options.
print(my_essay)

# <TRY IT OUT>
# declare a variable containing any number


# print the number


# replace the value of your variable with a string stating your name


# print the string


# finally: what happens if we reference a variable that hasn't been declared?
# the next line of code is 'commented out', remove the '# ' to 'comment it back in'
# and see what happens when python tries to execute it instead of ignoring it!
# your code editor may help you do this with the shortcut <ctrl+/>
# print(undeclared_variable)  # BOOM

# python will tell you it's not pleased with a 'stack trace',
# something like this:
### Traceback (most recent call last):
###   File "variables_ints_strings.py", line 31, in <module>
###     print(undeclared_variable) # BOOM
### NameError: name 'undeclared_variable' is not defined

# debugging takes practice, which we'll do plenty of!
# rule #1 is: when in doubt... print('it out!!')
# rule #2 is: that rule #1 isn't a good idea in some specific cases
