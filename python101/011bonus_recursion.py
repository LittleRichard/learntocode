
print('dont do this if you have a headache...')

# calling a function from itself is called recursion
# it is both convenient and DANGEROUS, because if you
# don't set up your exit criteria correctly it will
# call itself forever

def fibonacci(last, current):
    next_val = last + current
    print(f'next_val {next_val}')

    # if we don't have a way to break out,
    # this would run infinitely
    if next_val > 1000:
        return next_val

    # current becomes last, next becomes current,
    # and then we invoke it again.
    return fibonacci(current, next_val)

# invoke it once and then it will call itself
print('starts with: 1')
print('starts with: 1')
fibonacci(1, 1)

print('hopefully the movie Inception makes sense now.')
