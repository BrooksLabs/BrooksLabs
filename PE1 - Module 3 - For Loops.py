# FOR LOOP:
#   A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#   With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#   It can also "browse" large collections of data item by item.
#   Any variable after the for keyword is the control variable of the loop; it counts the loop's turns, and does it automatically;

print("The range instruction:")   
for i in range(3):
    print("The value of i is currently", i) # The range() function invocation may be equipped with two arguments, not just one.

print("\nThe continue instruction:")
for i in range(-2, 2):
    if i == 3:
        continue
    print("Inside the loop.", i) # continue - behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.
print("Outside the loop.")

print("\nExample #3:")    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # Print each fruit in a fruit list.
  
print("\nExample #4:")   
for x in "banana":
  print(x) # Loop through the letters in the word "banana".
  
print("\nExample #5:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break # Exit the loop when x is "banana".

print("\nExample #6:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # Do not print banana.
    
# NOTE:
    # print("\n") is used to create a newline.
    # range() can hold one or more positive and/or negative integer(s).