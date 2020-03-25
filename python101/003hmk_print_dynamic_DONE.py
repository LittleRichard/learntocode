# declare a variable that holds an integer of your choice
my_int = 10

# print your integer
print(my_int)

# declare a variable that holds a floating point number (anything with decimal places), AKA a float
my_float = 3.14159

# print your float
print(my_float)
## bonus points if you don't use %s
print('my float is %.5f' % my_float)


# declare a variable that holds a string of your choice
my_string = 'this is a string'

# print that string, injected into a template string
print('my string is: %s' % my_string)

# declare a variable that holds a template string including:
## some text
## a placeholder for a string
## a placeholder for a number
my_template = 'a string is: %s. a number is %d'


# print the template string WITHOUT injecting any values (no % after the template)
print(my_template)

# print the template string with values injected
print(my_template % (my_string, my_int))

# if you're curious, try customized formatting using the code you've already written
# here's some unofficial, but decent documentation. 
# http://www.thomas-cokelaer.info/tutorials/python/print.html#more-about-conversion-specifiers