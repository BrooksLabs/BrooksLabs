# THE WHILE LOOP:
#   With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i) # Print i as long as i is less than 6.
  i += 1
  
# THE BREAK STATEMENT:
#   With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break # Exit the loop when i is 3.
  i += 1
  
# THE CONTINUE STATEMENT:
#   With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # Continue to the next iteration if i is 3:
  print(i)
  
# THE ELSE STATEMENT:
#   With the else statement we can run a block of code once when the condition no longer is true:

    i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") # Print a message once the condition is false:
  
# THE INFINITE LOOP:
#   An endless loop, is a sequence of instructions in a program which repeat indefinitely (loop endlessly.)

while True:
    print("I'm stuck inside a loop.") # This loop cannot complete execution and will infinitely print "I'm stuck inside a loop." on the screen.

