print(2+2)

# An operator is a symbol of the programming language, which is able to operate on the values.
# For example, just as in arithmetic, the + (plus) sign is the operator which is able to add two numbers, giving the result of the addition.
# We'll begin with the operators which are associated with the most widely recognizable arithmetic operations: +, -, *, /, //, %, **
# Data and operators when connected together form expressions. The simplest expression is a literal itself.

print(2 ** 3)
# A ** (double asterisk) sign is an exponentiation (power) operator. Its left argument is the base, its right, the exponent.
# When both ** arguments are integers, the result is an integer, too; when at least one ** argument is a float, the result is a float, too.

print(6 // 3)
# A // (double slash) sign is an integer divisional operator. It differs from the standard / operator in two details:
# Its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded; it conforms to the integer vs. float rule.

print(14 % 4)
# The result of the operator is a remainder left after the integer division; the value left over after dividing one value by another to produce an integer quotient.
# This operator is sometimes called modulo in other programming languages.

# NOTES:
#   The result produced by the division operator / is always a float.
#   Rounding always goes to the lesser integer.
#   A unary operator is an operator with only one operand, e.g., -1, or +3.
#   A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.
