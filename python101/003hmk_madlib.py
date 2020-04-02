print('This is a bonus homework. Read and understand it for class, modify it for fun')

# the `print` function we've been using is one of a TON of functions
# that are built into python. the `input` function prompts someone
# executing the script from the command line for input, and then
# stores the result in a variable
test_input = input('Enter a test: ')
print(f'You entered {test_input}')

# why a variable for this but not others?
# because it's used more than once!
ask_noun_string = 'Enter a noun: '

# these are bad variable names, but in this case are perfectly
# descriptive so we aren't confused when we inject into our madlib
input1_noun1 = input(ask_noun_string)
input2_verb1 = input('Enter a verb (past tense): ')
input3_adj1  = input('Enter an adjective: ')
# notice how in the line above i added an extra space between the variable
# name and the `=` sign?  python doesn't care if you use extra spaces to 
# line things up, but later on spaces will matter so you have to be careful.
# TL;DR if it looks pretty and the script runs fine, good enough for me!
input4_noun2 = input(ask_noun_string)

my_madlib = f"""
I went to the store today and saw a {input1_noun1}, and as I
{input2_verb1} I asked: "Why do you always look so {input3_adj1}?"

But I never got a response, because suddenly there was no longer
a {input1_noun1} and a {input4_noun2} was sitting there looking at me!
"""
print(my_madlib)

# After several more classes, you will see several ways to improve
# this script using more complicated python. This would be a 
# PERFECT final project, choose your own difficulty and hopefully fun.
