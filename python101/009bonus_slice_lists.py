# mke a tuple with 10 elements, 0-9
my_tuple = tuple(range(10))

# grabs everything from the beginning up to, but not 
# including, the element at index 3
slice_from_start = my_tuple[:3]
print(f'slice [:3] is {slice_from_start}')

# same thing, grabs the value at index 3 to the end
slice_to_end = my_tuple[3:]
print(f'slice [3:] is {slice_to_end}')

 # python is forgiving and only goes to the end, but try
 # not to rely on this behavior because it's clumsy.
slice_out_of_bounds = my_tuple[4:1000]
print(f'slice [4:1000] is {slice_out_of_bounds}')

print('') # print a blank line

# slice all except the first and last
# starts at index 1 and goes up to, but not including,
# index -1
the_middle = my_tuple[1:-1]
print(f'slice [1:-1] is {the_middle}')

# slice using all negative indices
another_middle = my_tuple[-4:-1]
print(f'slice [-4:-1] is {another_middle}')
