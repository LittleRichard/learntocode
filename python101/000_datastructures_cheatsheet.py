
print("""
A summary of the data types & structures we've used

data type | mutable | iterable | ordered | Hashed  |
----------|---------|----------|---------|---------|
int       |  No     |  No      |  N/A    |  N/A    |
bool      |  No     |  No      |  N/A    |  N/A    |
float     |  No     |  No      |  N/A    |  N/A    |
str *     |  No     |  Yes     |  Yes    |  No     |
tuple     |  No     |  Yes     |  Yes    |  No     |
list      |  Yes    |  Yes     |  Yes    |  No     |
set       |  Yes    |  Yes     |  No     |  Yes    |
dict      |  Yes    |  Yes     |  No     |  Yes    |

* we haven't talked much about why strings are weird,
they're obviously a fundamental datatype but for a
variety of reasons related to performance and convenience,
they behave a lot like tuples.

Mutability is the property we explored with the mailboxes
and lockers, where the same data structure can have multiple
labels.

Iterability is whether or not you can for-loop over it

Ordered is whether or not the results will be in
predictable AND consistent order while iterating.

Hashed: uses key-based access to store/access elements,
versus zero-based-index access.
""")
