# EQUALITY: The equal to operator (==)
#   The == (equal to) operator compares the values of two operands. If they are equal, the result of the comparison is True. If they are not equal, the result of the comparison is False.

var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

# INEQUALITY: The not equal to operator (!=)
#   The != (not equal to) operator compares the values of two operands, too. Here is the difference: if they are equal, the result of the comparison is False. If they are not equal, the result of the comparison is True.

var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)

# COMPARISON OPERATORS: Greater than
#   You can also ask a comparison question using the > (greater than) operator.
#   If you want to know if there are more black sheep than white ones, you can write it as follows:

black_sheep = 2
white_sheep = 1
print(black_sheep > white_sheep) # If the program returns True, it confirms it; False denies it.

# COMPARISON OPERATORS: Greater and Less than or equal to
#   The greater than operator has another special, non-strict variant, but it's denoted differently than in classical arithmetic notation: >= (greater than or equal to).
#   The less than operator also has a special, non-strict variant, but it's denoted differently than in classical arithmetic notation: <= (less than or equal to).
#   Both of these operators (strict and non-strict), are binary operators with left-sided binding, and their priority is greater than that shown by == and !=.

a = input("Enter a numerical value: ")
b = input("Enter a smaller numerical value: ")
print(a >= b)
