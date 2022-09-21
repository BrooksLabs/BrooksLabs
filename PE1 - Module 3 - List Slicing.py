# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Using negative values for both start and end is possible (just like in indexing).
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# If you omit the "start" in your slice, it is assumed that you want to get a slice beginning at the element with index 0.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

# If you omit the "end" in your slice, it is assumed that you want the slice to end at the element with the index len(my_list).
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# The del instruction is able to delete more than just a list's element at once - it can delete slices and/or the list itself.
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Deleting all the elements at once is possible too.
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# THE "in" AND "not in" OPERATORS:
#   These operators are able to look through the list in order to check whether a specific value is stored inside the list or not by returning True or False.
my_list = [10, 8, 6, 4, 2]
print(5 in my_list)
print(5 not in my_list)
print(10 in my_list)

# NOTES:

#   A slice makes a new (target) list, taking elements from the source list - the elements of the indices from start to end - 1.
#   An element with an index equal to end is the first element which does not take part in the slicing (Not to "end" but to "end - 1").