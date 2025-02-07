# First, create a file named match.py with this content:
Value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _:  # default case
        print('value is neither 5 or 6')
# value is 5

# This example is functionally identical to the following if/else statement:

value = 5

if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')
# value is 5

# You can see how similar they are, but you can also see how they differ. The match statement evaluates the expression value,
# compares its value to the value in each case, and executes the block associated with the first matching case. In this example, the value of the expression is 5;
# thus, the program executes the statements associated with case 5. The statements in the case _ block run when the expression doesn't match any other case blocks.
# It acts like the final else in an if statement and must be the last case block in the match statement.

# If you want to match multiple values in a case, you can do so by using the | character to separate item values:

value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:  # default case
        print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6

# There are plenty of uses for match statements. They also have "pattern matching" abilities (which are beyond the scope of this book).
# They're potent tools in Python. If you're uncomfortable with them, play with the ones we presented above and watch how they respond to your changes.
# Test their boundaries and learn their capabilities. Curiosity will serve you well in your journey towards mastering Python. There is much to discover!
