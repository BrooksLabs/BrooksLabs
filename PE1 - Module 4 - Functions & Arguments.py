# FUNCTIONS:
#   A function is a block of code that performs a specific task when the function is called (invoked). You can use functions to make your code reusable, better organized, and more readable. Functions can have parameters and return values.
#   There are at least four basic types of functions in Python (You can see a complete list of Python built-in functions at https://docs.python.org/3/library/functions.html).

# - Built-in functions which are an integral part of Python (Such as the "print()" or "input()" functions).
# - The ones that come from pre-installed modules.
# - User-defined functions which are written by users for users (You can write your own functions and use them freely in your code).
# - The lambda functions.

# THE lambda FUNCTION:
#   lambda is a small anonymous function that can take any number of arguments, but can only have one expression.

x = lambda a : a + 10 # x = lambda arguments : expression
print(x(5)) # a = 5 (5 + 10 = 15)

x = lambda a, b : a * b
print(x(5, 6)) # a = 5, b = 6 (5 * 6 = 30)

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # a = 5, b = 6, c = 2 (5 + 6 + 2 = 13)

# USING "def" & CALLING A FUNCTION:
    # In Python a function is defined using the "def" keyword.
    # To call a function, use the function name followed by parenthesis.
    
def my_function():
  print("\nThis is a basic function.")

my_function()

# ARGUMENTS:
#   Information can be passed into functions as arguments.
#   Arguments are specified after the function name, inside the parentheses (You can add as many arguments as you want, just separate them with a comma).
#   The following example has a function with one argument (Firstname):

def my_function(Firstname): # When the function is called, we pass along a first name, which is used inside the function to print the full name.
  print(Firstname + " Lastname")

my_function("John")
my_function("Jane")
my_function("Joe")

# KEYWORD ARGUMENTS:
#   You can also send arguments with the key = value syntax.
#   This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "John", child2 = "Jane", child3 = "Joe")