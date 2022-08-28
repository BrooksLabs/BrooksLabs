client_name = input('Hello! What is your name?: ')
account_balance = input('Enter a number for your account balance: ')
print(client_name + "'s account balance is $" + str(account_balance))

# Python offers special "boxes" (containers) to save the intermediate results, and use them again to produce subsequent ones. These boxes are called variables.
# This example uses the input() method to ask for the user's name and a value for it's variables. When entered, they are printed on the screen respectively using concatination.

# If you want to give a name to a variable, you must follow some strict rules:
#   - The name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
#   - The name of the variable must begin with a letter;
#   - The underscore character is a letter;
#   - Upper- and lower-case letters are treated as different (a little differently than in the real world - Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
#   - The name of the variable must not be any of Python's reserved keywords.

# NOTES:
#   You can only concatenate str (not "float") to str.
#   The easiest way to convert int to a string is using str() function: print(a + str(b))