print("2") # A "string"
print(2) # An "integer number"

# Prints two different types of literals.

# There are also two additional conventions:
    
print(0o123) # Allows us to use numbers in an octal representation.

# - If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value.
# - This means that the number must contain digits taken from the [0..7] range only.
# - 0o123 is an octal number with a (decimal) value equal to 83.
# - The print() function does the conversion automatically.

print(0x123) # Allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).

# - 0x123 is a hexadecimal number with a (decimal) value equal to 291.
# - The print() function can manage these values too.


# KEY TAKEAWAYS
#   - Literals are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., "123"), or a string (string literals, e.g., "I am a literal.").

#   - The binary system is a system of numbers that employs 2 as the base. Therefore, a binary number is made up of 0s and 1s only, e.g., "1010" is 10 in decimal.
#     Octal and hexadecimal numeration systems, similarly, employ 8 and 16 as their bases respectively. The hexadecimal system uses the decimal numbers and six extra letters.

#   - Integers (or simply ints) are one of the numerical types supported by Python. They are numbers written without a fractional component, e.g., "256", or "-1" (negative integers).

#   - Floating-point numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers that contain (or are able to contain) a fractional component, e.g., "1.27".

#   - To encode an apostrophe or a quote inside a string you can either use the escape character, e.g., 'I\'m happy.', or open and close the string using an opposite set of symbols to the ones you wish to encode, e.g., "I'm happy." to encode an apostrophe, and 'He said "Python", not "typhoon"' to encode a (double) quote.

#   - Boolean values are the two constant objects True and False used to represent truth values (in numeric contexts 1 is True, while 0 is False.

# NOTE:
#   The "None" literal. This literal is a so-called NoneType object, and it is used to represent the absence of a value.
