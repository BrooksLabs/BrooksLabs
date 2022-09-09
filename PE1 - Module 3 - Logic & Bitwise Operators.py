# Python supports the following logical operators:
    
#   - and → if both operands are true, the condition is true, e.g., (True and True) is True,
#   - or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
#   - not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
#   - xor → returns 1 if one of the bits is 1 and the other is 0 else returns false.

# BITWISE OPERATORS
#   You can use bitwise operators to manipulate single bits of data.

a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)
# Print bitwise OR operation
print("a | b =", a | b)
# Print bitwise NOT operation
print("~a =", ~a)
# print bitwise XOR operation
print("a ^ b =", a ^ b)

# SHIFT OPERATORS
#   The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.
#   This is applied only to integer values, and you mustn't use floats as arguments for it.
#   Multiplying by ten is in fact a shift of all the digits to the left and filling the resulting gap with zero; Dividing by ten is also simply shifting the digits to the right.

a = 10
b = -10
 
# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
 
a = 5
b = -10
 
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)