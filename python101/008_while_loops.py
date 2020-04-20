import random

# a for loop runs over a finite set of values,
# but what if we aren't sure when we want to stop?

# the while loop runs until a boolean expression is met,
x = 0
while x < 5:
    # equivalent to:
    # `x = x + 1`
    x += 1
    print(f'while x < 5: {x}')

# maybe a better example
total = 0
while total < 100:
    # equivalent to:
    # `total = total + random.randint(0, 25)`
    total += random.randint(0, 25)
    print(f'total so far {total}')

print(f'final total: {total}')

# the break statement halts a loop immediately
while 1 > 0:
    print('executes once before hits a `break` statement')
    break

while 0 > 1:
    print('never executes, the condition is never met')

# the continue statement immediately stops a loop
# and skips to the next iteration
for x in range(5):
    if x == 3:
        continue

    print(f'range(5) skip 3: {x}')

print(f'`break` and `continue` are handy, but use sparingly...')
print(f'if you need lots of break/continue, there might be an easier way')


print("""
the while loop runs until a boolean expression is met,
in constrast with the for loop that runs an exact number
of times. choose wisely!""")

# a mistake everyone will make at least once
# lets loop until we hit a value
rand_val = 0  # hold a random int each loop
counter = 0  # number of tries it took
while rand_val != 100000:
    rand_val = random.randint(1, 10000)
    counter += 1

    if counter % 100000 == 0:
        print(f'Update! counter: {counter}')

    # but there is a bug here!
    # the max randint is missing a zero,
    # so the while loop's condition will always
    # be met

    # ctrl-c to tell the terminal to kill your python
    # process by 'throwing an error'
    if counter % 1000000 == 0:
        # python can do a simple loop several million
        # times in under a minute on most computers,
        # which is slower than other languages but still
        # fast enough to do some heavy lifting.
        print(f'Hit <ctrl-c> to force-quit!')


print('this line will never be printed!')
print('the program either loops to infinity or is killed.')

print("""
get used to littering your program with prints, debug
messages with specific values are a great way to track
what your program is doing, especially while looping.
""")