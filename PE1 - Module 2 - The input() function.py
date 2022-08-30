print("What is today's date?") # print() function
date = input() # input() function
day = input("What day of the week is it? ") # This method merges the print() and input() into one line.
print("Today is", day, "~ " + date)

#   The input() function is a mirror reflection of the print() function; print() sends data to the console, input() gets data from it.
#   The input() function is able to read data entered by the user and to return the same data to the running program.
#   Virtually all programs read and process data. A program which doesn't get a user's input is a deaf program.
#   The program will prompt the user to input some data from the console (most likely using a keyboard, although it is also possible to input data using voice or image).

# TYPE CASTING:
#   The int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer; if it fails, the whole program will fail too.
#   The float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float (the rest is the same).

# CONCATENATION:
#   The + (plus) sign, when applied to two strings, becomes a concatenation operator: string + string

# REPLICATION:
#   The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator.

print("This lesson is on replication:")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# NOTES:
#   The result must be assigned to a variable or else the entered data will be lost.
#   The result of the input() function is also a string.
#   In contrast to its arithmetic sibling, the concatenation operator is not commutative, i.e., "ab" + "ba" is not the same as "ba" + "ab".
