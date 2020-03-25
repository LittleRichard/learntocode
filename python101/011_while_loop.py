import random
import time
import math

# a for-loop iterates over a set of data,
# which means it has a fixed range.

# a while-loop iterates until a condition is met
# and then ends.

# init a static constant (all caps!), which
# will be our way of tuning the while loop's
# number of iterations
# math.pow is an exponent, in this case like 10 ^ 6 = 1 million
LOOP_SIZE_PARAM = math.pow(10, 6) # not precise, tunes a randomizer

# while (an expression evaluating to True or False):
#     print('execute code in this block')
# BE CAREFUL!!!!!!!!!!!!!
# if you're expression never evaluates to False, you'll
# have an INFINITE LOOP. Sometimes this is intentional and good,
# like in a web application that listens for requests forever.

# grab the current time
start_time = time.time()
# this variable will track the number of loops we've made
loop_count = 0

# init the variable to a value that will
# satisfy the loop condition
my_rand_int = 1 # not random yet
while my_rand_int != 0:
    loop_count = loop_count + 1

    # pull a new random value
    my_rand_int = random.randint(0, LOOP_SIZE_PARAM)
    # as soon as we randomly pull a zero, we break
    # out of the while loop

end_time = time.time()

elapsed_time = end_time - start_time
print('%d loops took %.5f seconds' % (loop_count, elapsed_time))

num_million_loops = loop_count / 1000000.0 # floating point division to avoid rounding errors
print('million loops per second: %.3f' % (num_million_loops / elapsed_time))

# see how this for-loop and while-loop are the same?
for x in xrange(1, 11):
    print(x)

y = 1
while y < 11:
    print(y)
    y = y + 1

print('hit ctrl+C to force-quit in the terminal')
z = 1
while z != 10:
    z = z + 2 # 1,3,5,7,9,11
print('the above is an infinite loop... this line will never be reached')