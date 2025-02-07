value1 if conditions else value2

# Python first evaluates the condition. If it's truthy, the expression returns value1. Otherwise, it returns value2.
# Note that only one of value1 and value2 will be evaluated.

# Consider the following code:

if shape.sides() == 3:
    print("Triangle")
else:
    print("Square")

# That's easy enough to understand, but it is a bit wordy. We can eliminate the wordiness at the sacrifice of a little clarity:

print("Triangle" if shape.sides() == 3 else "Square")

# Ternaries work particularly well when you need a way to handle missing or invalid data in output:

print('N/A' if value == None else value)

# Should you use ternary expressions in your code? We recommend using them only when it doesn't sacrifice too much clarity.
# Don't use them as a substitute for every 4-line if/else statement or as a way to save keystrokes: they work best as expressions.

# Remember that many Python programmers dislike ternary expressions since they are hard to read. If you decide that you like ternary expressions, that's fine.
# However, use them judiciously. In particular, ternaries should almost always be extremely simple and fit entirely on one 79-column line of code.
