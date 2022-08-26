print("2")
print(2)

# Prints two different types of literals:

# 1.) A "string"
# 2.) An "integer number"

# There are two additional conventions:
    
    print(0o123)
    
#       1.) Allows us to use numbers in an octal representation.

#       If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value.
#       This means that the number must contain digits taken from the [0..7] range only.
#       0o123 is an octal number with a (decimal) value equal to 83.
#       The print() function does the conversion automatically.

    print(0x123)

#       2.) Allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).

#        0x123 is a hexadecimal number with a (decimal) value equal to 291.
#        The print() function can manage these values too. Try this: