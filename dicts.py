

###
plants = {}

# Add three key-value tuples to the dictionary.
plants["radish"] = 2
plants["squash"] = 4
plants["carrot"] = 7

# Get syntax 1.
print(plants["radish"])

# Get syntax 2.
print(plants.get("tuna"))
print(plants.get("tuna", "no tuna found"))



### key error
lookup = {"cat": 1, "dog": 2}

# The dictionary has no fish key!
print(lookup["fish"])


### in
animals = {}
animals["monkey"] = 1
animals["tuna"] = 2
animals["giraffe"] = 4

"tuna" in animals


### Len built-in.
animals = {"parrot": 2, "fish": 6}

# Use len built-in on animals.
print("Length:", len(animals))



### .keys(), .values(), .items()
hits = {"home": 125, "sitemap": 27, "about": 43}
keys = hits.keys()
values = hits.values()


rents = {"apartment": 1000, "house": 1300}

# Convert to list of tuples.
rent_items = rents.items()

for item in rent_items:
    print("Place:", item[0])
    print("Cost:", item[1])
    print("")



### update()


# First dictionary.
pets1 = {"cat": "feline", "dog": "canine"}

# Second dictionary.
pets2 = {"dog": "animal", "parakeet": "bird"}

# Update first dictionary with second.
pets1.update(pets2)

# Display both dictionaries.
print(pets1)
print(pets2)
