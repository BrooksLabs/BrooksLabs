a = input("Enter a numerical value: ")
b = input("Enter a smaller numerical value: ")


# CONDITIONAL EXECUTIONS:
#   When a specific condition is met or not, e.g., you go for a walk if the weather is good, or stay home if it's wet and cold.
#   The first form of a conditional statement, which you can see below is written very informally but figuratively:

if a >= b:
    print(a, "is greater than or equal to",  b)
else:
    print("ERROR!", b, "is greater than or equal to",  a)

# This conditional statement consists of the following, strictly necessary, elements in this and this order only:
    
#   - The "if" keyword;
#   - One or more white spaces;
#   - An expression (a question or an answer) whose value will be interpreted solely in terms of True (when its value is non-zero) and False (when it is equal to zero);
#   - A colon followed by a newline;
#   - An indented instruction or set of instructions (at least one instruction is absolutely required); the indentation may be achieved in two ways - by inserting a particular number of spaces (the recommendation is to use four spaces of indentation), or by using the tab character; note: if there is more than one instruction in the indented part, the indentation should be the same in all lines; even though it may look the same if you use tabs mixed with spaces, it's important to make all indentations exactly the same - Python 3 does not allow mixing spaces and tabs for indentation.

# If the true_or_not expression represents the truth (i.e., its value is not equal to zero), the indented statement(s) will be executed;
# If the true_or_not expression does not represent the truth (i.e., its value is equal to zero), the indented statement(s) will be omitted (ignored), and the next executed instruction will be the one after the original indentation level.

