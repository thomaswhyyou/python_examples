# Both of these are strings
string_double_quote = "Hello world"
string_single_quote = 'Hello world'


# You can make an empty string like this
empty_string = ""
empty_string = str()


# Python strings are immutable
a = "some random text"
b = a
id(a), id(b)
a == b  # True
a is b  # True

b += ", and concatenate more strings"

a  # "some random text"
b  # "some random text, and concatenate more strings"
id(a), id(b)


# Python string interpolation
name = "Carmen"
age = 16

"I have a dog and her name is {}. She is {} years old.".format(name, age)
"I have a dog and her name is {1}. She is {0} years old.".format(name, age)
"I have a dog and her name is {dog_name}. She is {dog_age} years old.".format(dog_age=age, dog_name=name)

sentence = "I have a dog and her name is {}. She is {} years old."
print(sentence)
print(sentence.format(name, age))

asdf = "penut" + " butter"
"penut" * 3


# Python string -> iterable
word = "internationalization"
len(word)  # Maybe awkward for Rubists at first
word[5]
word[-1]
word[2:]
word[2:6]
for char in word:
    print(char)

# Common operation
word.replace("inter", "")
word.split("liza")
word.split("n")
"$".join(word.split("n"))  # Definitely awkward

"nation" in word  # True
"hotdog" in word  # False

another_word = "hello, World"
another_word.lower()
another_word.upper()
another_word.capitalize()
another_word.title()
