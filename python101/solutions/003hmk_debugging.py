# This code has a few bugs in it.  Some are syntax errors, which
# mean that python won't run it and will tell you why.  Some
# make the result of this program not make sense.  

# Learning how to debug code is the most fundamental skill 
# of software development.

# Fix this script so that it runs to completion and makes sense. You
# can fix it (mostly) however you like, as long as it uses string interpolation
# to print the following 3 statements:
# # a correct math equation
# # a realistic observation
# # something truthful

# Tip: Renaming some variables might help you stay sane, but be careful
# you rename ALL references to that variable!

a = 300
b = 5.3
d = 60
c = 2 * b
# you could do pretty much anything you want to these 
# variables, as long as it works
d = b

# DONT MODIFY THE NEXT LINE
print(f'{a} + {d} - {c} = 294.7')


animal1 = 'horse'
animal5 = 'mouse'
my_animal = f'{animal1}{animal5}'
action1 = 'call the biologists'

# DONT MODIFY THE NEXT LINE
print(f'When {my_animal} fly, we should {action1}')


play_str = 'games'
watch_str = 'sports'
esp_with_str = 'a tall, cool budweiser'

# You might need to modify the contents of this string a little
c = f'I like to play {play_str} and watch {watch_str}, especially with {esp_with_str}'
print(c)

# that sneaky line at the end that was doing 1 / 0 wasnt doing anything,
# so i showed no mercy