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

print("The first element in this list is:", numbers[0]) # Accessing the list's first element.

# THE len() FUNCTION:
#   This function is used to check the list's current length.
#   len() uses the list's name as an argument, and returns the number of elements currently stored inside the list.

print("List length:", len(numbers), "elements")  # Printing the list's length.

# THE del() INSTRUCTION / REMOVING ELEMENTS FROM A LIST:
#   Any of the list's elements may be removed at any time with an instruction named del (delete).

del numbers[1]  # Removing the second element from the list.
print("\nNew List:", numbers)  # Printing current list content.
print("New List length:", len(numbers), "elements") # Printing new list length.

# NEGATIVE INDICIES:
#   Negative indices are legal; An element with an index equal to -1 is the last one in the list.
#   Similarly, the element with an index equal to -2 is the one before last in the list.
#   The last accessible element in our list is numbers[-4] (the first one) - don't try to go any further!

numbers = [-1, 2, 3, 4]
print("The last value in this list is:", numbers[-1])
print("The second-to-last value in this list is:", numbers[-2])

# LIST METHODS:
#   - A method is a specific kind of function - it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.
#   - A function doesn't belong to any data - it gets data, it may create new data and it (generally) produces a result.
#   - A method does all these things, but is also able to change the state of a selected entity.
#   - A method is owned by the data it works for, while a function is owned by the whole code.

# ADDING ELEMENTS TO A LIST: append() AND insert()

numbers = [1, 2, 3, 4]
print("")
print(numbers)
print("This list has", len(numbers), "elements")

numbers.append(5) # Append 5 to the end of the list.
print("")
print(numbers)
print("The appended list has", len(numbers), "elements")

numbers.insert(0, -1) # Insert -1 as the first element.
print("")
print(numbers)
print("This list has", len(numbers), "elements")

# CREATING AN EMPTY LIST:
    
my_list = [] #creating an empty list

for i in range(5):
    my_list.append(i + 1) # creates a list of 4 elements that increases by 1 using the for loop.

print("")
print(my_list)
print("This list has", len(my_list), "elements")
