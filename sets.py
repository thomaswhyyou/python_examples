
## Quick example
# Create a set.
items = {"arrow", "spear", "arrow", "arrow", "rock"}

# Print set.
print(items)
print(len(items))

# Use in-keyword.
if "rock" in items:
    print("Rock exists")

# Use not-in keywords.
if "clock" not in items:
    print("Cloak not found")


## Using add
# An empty set.
items = set()

# Add three strings.
items.add("cat")
items.add("dog")
items.add("gerbil")
print(items)



## subset, superset
numbers1 = {1, 3, 5, 7}
numbers2 = {1, 3}

# Is subset.
if numbers2.issubset(numbers1):
    print("Is a subset")

# Is superset.
if numbers1.issuperset(numbers2):
    print("Is a superset")


## Union
# Two sets.
set1 = {1, 2, 3}
set2 = {6, 5, 4, 3}

# Union the sets.
set3 = set1.union(set2)
print(set3)


## subract
a = {"new york", "connecticut", "new jersey"}
b = {"connecticut", "pennsylvania", "maine"}

# Subtract.
c = a - b
print(c)

# Difference.
c = a.difference(b)
print(c)

# Subtract in opposite order.
c = b - a
print(c)
