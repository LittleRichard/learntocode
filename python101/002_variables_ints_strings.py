# in python, anything following a '#' is a code comment and is ignored
# by python's interpreter.  code comments are notes for the next developer.

# this file is a script. script is an apt name for it, since you'll
# decide who is in your script, what they say, and in which order they say it.
# python is kinda dumb and does exactly what you tell it to.

# it can be executed by python from the command line as:
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
all_ones = 111
print('all_ones')
print(all_ones)  # prints the contents of the variable 'all_ones', which is 111

# define another variable
all_twos = 222
print('all_twos')
print(all_twos)  # prints the contents of the variable 'all_twos', which is 222

# variables can be overwritten to different value
my_third_var = 333
print('my_third_var')
print(my_third_var)  # prints my_third_var's current value, 333
print('my_third_var (the 2nd time)')
my_third_var = -444  # a negative number!
print(my_third_var)  # prints my_third_var's current value, 444

# assign a variable into another!
all_twos = all_ones
print('after all_twos = all_ones')
print(all_twos)  # prints 111

# the original variable retains its value
print('all_ones again')
print(all_ones)  # prints 111
# not always true for more advanced datatypes, but we'll get there

# a quick note on variable names:
# # 1) choice of variable names is often the difference between good
# # developers and bad ones.  do future-yourself a favor and don't
# # do things like:
num1 = 10
num2 = -10
# # because 50 lines of code later you might forget
# # and show someone your social security number 
# # 2) you don't have to use a variable, like these 2 we just declared, 
# # but if you don't use it... why is it even there? some code editors
# # will highlight this for you.

# STRINGS
# variables can also be text, called 'strings', and are defined one of 3 ways
print('the hello world we printed at the beginning was a string')
print('this is how you put a "new line" character in a string: \nsee?')

my_single_quoted_string = 'this is a string that says "this is a string"'  # note the use of ""
print(my_single_quoted_string)

my_double_quoted_string = "a double quoted string won't care about single quotes"  # note the ' char in the middle
print(my_double_quoted_string)

my_manuscript = """Triple quotes are very useful for when you
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
print(my_manuscript)

my_masterpiece = """
                _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
"""
print('"ASCII ART" is kind of a primitive meme')
print(my_masterpiece)

# your code editor might be alarmed by my masterpiece, because it
# includes an "escape character", in this case the '\', which tells
# python to treat the following character literally. for example, even 
# if it's a single quote in a single-quoted string.
# Don't dwell on this for now:
my_escaped_quote_string = 'This won\'t break, and prints with only one backslash: \\'
print(my_escaped_quote_string)

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
print('Uncomment the line above this one to see the BOOM')

# python will tell you it's not pleased with a 'stack trace',
# something like this:
### Traceback (most recent call last):
###   File "variables_ints_strings.py", line 31, in <module>
###     print(undeclared_variable) # BOOM
### NameError: name 'undeclared_variable' is not defined

# debugging takes practice, which we'll do plenty of!
# rule #1 is: when in doubt... print('it out!!')
# rule #2 is: that rule #1 isn't a good idea in some specific cases
