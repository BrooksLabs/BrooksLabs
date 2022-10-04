# DICTIONARIES & KEY-VALUE PAIRS:
#   The dictionary is a mutable Python data structure (It's not a sequence type, but can be easily adapted to sequence processing).
#   A dictionary is also a set of key-value pairs (In python, the word you look for is named a key, and the word you get from the dictionary is called a value).

# NOTES:
#   - Each key must be unique (it's not possible to have more than one key of the same value).
#   - A key may be any immutable type of object: it can be a number (integer or float), or even a string, but NOT a list.
#   - A dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values.
#   - The len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary.
#   - A dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.
#   - Keys are case-sensitive, and you can't use non-existent keys.

# The first of our dictionaries is a very simple English-Spanish dictionary:
dictionary = {"cat": "gato", "dog": "perro", "horse": "caballo"} # The list of pairs is surrounded by curly braces{}, while the pairs themselves are separated by commas, and the keys and values by colons.
# The second is a very tiny telephone directory:
phone_numbers = {'Mom': 5551234567, 'Dad': 22657854310}
# The empty dictionary is constructed by an empty pair of curly braces:
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# If you want to get any of the values, you have to deliver a valid key value:
print("Mom's number is:", phone_numbers['Mom'])
print("The Spanish word for cat is:", dictionary['cat'])

# IN & NOT IN OPERATORS:
#   The following code safely searches for some Spanish words and will prompt users if a word isn't in the dictionary:
    
words = ['cat', 'dog', 'horse', 'cow']    
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in our dictionary")