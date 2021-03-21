# this is NOT a built-in, and must be installed from the CLI:
# $ pip3 install cmd2
import cmd2
import datetime
import sys

# this script will cover the cmd2 library, and because
# it uses Object Oriented programming, we'll touch on
# some fundamentals of OO.

not_used_variable = """
Object oriented code is a way of thinking about code, not a 
different language or syntax. Instead of thinking about
your variables as data, try to imagine them as objects;

Objects can have 'properties', as well as functions defined
on them. We've actually been doing this for a while with
lists and .append()

A 'class' is the definition and description of an object.
Initializing a class gives you an 'instance' of the class.
"""

# you can declare your own objects using the 'class' keyword,
# and in this case we're going to say that MyClass inherits
# from the (builtin) object class
class MyClass(object):

    # define an init function; this is called when you create
    # a new instance of the class.  it must be called __init__,
    # that's how python knows how to find it.
    def __init__(self, my_value):
        # self is how you reference this instance of the class
        # from inside the class; it doesn't exist outside
        # the class

        print(f'initializing a MyClass instance with {my_value}')

        # set the input my_value into a property of THIS
        # instance of the class
        self.my_value = my_value

        # gets the current time in UTC timezone and stores it
        self.time_created = datetime.datetime.utcnow()

    def get_desc(self):
        return f'my value {self.my_value}, created at {self.time_created}'

my_class1 = MyClass(1)
my_class2 = MyClass(2)

print(my_class1.my_value)
my_class1.my_value = 111111
print(my_class1.time_created)
print(my_class1.get_desc())
print('')

print(my_class2.my_value)
my_class2.my_value = 222222
print(my_class2.time_created)
print(my_class2.get_desc())

print("""
There is a LOT more complexity to OO, but knowing about these
should get you started:
- class vs. instance
- self
- property
- functions in classes

If you make a class that 'inherits' from another, it is a 'subclass'
of the parent class and has a copy of all functions from the parent!
""")

print("""
cmd2 is a library that does all the hard part of creating a command
line interface in python, so you can focus on building functionality.
""")

# create your cmd2 class, which should 'inherit' from a class
# provided by the library.
class MyCmd2(cmd2.Cmd):

    def __init__(self, app_name, app_desc):

        # call the parent class' __init__ because it does
        # a bunch of important stuff. bits and bytes, but 
        # you should pretty much always do this in an __init__
        # of a subclass
        super().__init__()

        self.name = app_name
        self.desc = app_desc

        # sets the prompt you see at this app's CLI
        self.prompt = f'{self.name} # '

    # functions that start with 'do_' are exposed
    # as CLI functions automagically!
    def do_summary(self, args):
        print(f"This app's name is {self.name}. {self.desc}")

# and then once we've created the class, we make an instance
cmd = MyCmd2('test app', 'this is just a demo')

# and then invoke it's 'cmdloop' function to run it
# try typing 'help'
print('starting CLI, use "quit" command to exit')
cmd.cmdloop()

print("""
cmd2 is a great way to build an application that will
interact with the user; you can modify the properties
of the class to store data/state, and build functions 
to fulfill various actions/commands.

Imagine this as a harness for a game like blackjack and hopefully
that starts to make the power of it more clear.
""")