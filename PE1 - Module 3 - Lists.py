# LISTS:
#   A list is a collection of elements, but each element is a scalar.
#   A list starts with an open square bracket and ends with a closed square bracket; the space between the brackets is filled with values separated by commas).
#   The elements inside a list may have different types. Some of them may be integers, others floats, and yet others may be lists.

numbers = [0, 1, 2, 3, 4]  # a list consisting of five values, all of them numbers.

# Python has adopted a convention stating that the elements in a list are always numbered starting from zero. This means that the item stored at the beginning of the list will have the number zero. Since there are five elements in our list, the last of them is assigned the number four. 

# INDEXING:
#   To change the value of a chosen element in a list, you must first assign a new value to the first element (0).

numbers = [0, 1, 2, 3, 4]
print("Original List:", numbers)  # Printing original list content.

numbers[0] = -1
print("\nNew list: ", numbers)  # Current list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("\nCurrent List:", numbers)  # Printing current list content.

# ACCESSING LIST CONTENT:
#   Each of the list's elements may be accessed separately.

print("\nThe first element in this list is:", numbers[0]) # Accessing the list's first element.

# THE len() FUNCTION:
#   This function is used to check the list's current length.
#   len() uses the list's name as an argument, and returns the number of elements currently stored inside the list.

print("List length:", len(numbers))  # Printing the list's length.

# THE del() INSTRUCTION / REMOVING ELEMENTS FROM A LIST:
#   Any of the list's elements may be removed at any time with an instruction named del (delete).

del numbers[1]  # Removing the second element from the list.
print("\nNew list content:", numbers)  # Printing current list content.
print("New list's length:", len(numbers))  # Printing new list length.

# NEGATIVE INDICIES:
#   Negative indices are legal; An element with an index equal to -1 is the last one in the list.
#   Similarly, the element with an index equal to -2 is the one before last in the list.
#   The last accessible element in our list is numbers[-4] (the first one) - don't try to go any further!

numbers = [-1, 2, 3, 4]
print(numbers[-1])
print(numbers[-2])

    