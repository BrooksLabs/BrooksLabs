# SEQUENCE TYPES AND MUTABILITY:
#   A sequence type is a type of data in Python (Scanned by the "for" loop) which is able to store more than one value (or less than one, as a sequence may be empty).
#   These values can be sequentially browsed, element by element.
#   Mutability is a property of any of Python's data that describes its readiness to be freely changed during program execution at any time (we call such an operation in situ).
#   There are two kinds of Python data: mutable and immutable (Immutable data cannot be modified in this way).

fruits = ["apple", "banana", "orange"]
fruits.append("grape") # list.append(elmnt) - This example modifies the data in a list by adding an element of any type (string, number, object etc).
print(fruits)
print("This list has:", len(fruits), "elements.") # The len() function is used to determine how many elements the list contains.

# TUPLES:
#   A tuple is an immutable sequence type that can behave like a list, but it's elements cannot be changed, added or removed after it's creation).
#   Tuples prefer to use parenthesis(), whereas lists like to see brackets[].
#   It's also possible to create a tuple from a set of values separated by commas.
#   Tuples are ordered; the items have a defined order, and that order will not change.
#   Since tuples are indexed, they can have items with the same value.

meats = ("beef", "fish", "turkey")
print(meats)
print("This tuple has:", len(meats), "elements.") # The len() function is used to determine how many elements the tuple contains.

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple:
vegetables = ("onion",)  # <- prints a tuple
print(type(vegetables))

vegetables = ("onion") # <- prints a string; NOT a tuple
print(type(vegetables))

# It is also possible to create an empty tuple - parentheses are required then:
empty_tuple = ()
print()

# NOTES:
# - The len() function accepts tuples and/or lists, and returns the number of elements contained inside.
# - The "+" operator can join tuples together.
# - The "*" operator can multiply tuples, just like lists.
# - The "in" and "not in" operators work in the same way as in lists.
# Example:
    
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
print("Our final tuple has:", len(t2), "elements.")
