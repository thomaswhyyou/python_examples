

## Create
# Zero-element tuple.
a = ()
# One-element tuple.
b = ("one",)
# Two-element tuple.
c = ("one", "two")


## Immutability
tuple = ('cat', 'dog', 'mouse')

# This causes an error.
tuple[0] = 'feline'


## Pack, unpack
# Create packed tuple.
pair = ("dog", "cat")

# Unpack tuple.
(key, value) = pair


## Tuple is created by comma separation
# A trailing comma indicates a tuple.
one_item = "cat",

# A tuple can be specified with no parentheses.
two_items = "cat", "dog"

print(one_item)
print(two_items)
