# A conditional is a fork, or multiple forks, in the road. When your data arrives at a conditional, Python evaluates the conditional and tells the data where to go.
# The simplest conditionals use a combination of if statements with comparison and logical operators (<, >, <=, >=, ==, !=, and, or, and not) to direct traffic.
# They use the keywords if, elif, and else.

# That's enough talking; let's write some code. Create a file named conditional.py with the following content:

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')

# Run conditional.py at least twice.

# The first time, enter the value 3.
# The second and subsequent times, input any other integer value.
# This example shows the simplest of if statements: it has a single block (one or more Python statements or expressions)
# that executes when the condition (value == 3) is True. Otherwise, Python bypasses the block.
# Regardless, execution eventually resumes with the first statement or expression after the if statement.

# Thus, if the input value is 3, this code prints value is 3. The code doesn't print anything if the user inputs any other integer.

# We can expand the if statement to include some code that runs when value is not 3:

value = int(input('Enter a number: '))


if value == 3:
    print('value is 3')
else:
    print('value is NOT 3')

# Here, Python prints value is 3 if the user enters 3; otherwise, it prints value is NOT 3.

# Note that the else block isn't a proper statement; it's part of the if statement.

# We can nest if statements inside an outer if. In this next example, we nest an if statement inside the else block of the outer if:

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')


# This time, run conditional.py at least three times:

# The first time, enter the value 3.
# The second time, enter the value 4.
# The third and subsequent times, input any other integer value.
# The indentation levels show how the code is supposed to work. In this case, Python:

# prints value is 3 if the user inputs 3.
# prints value is 4 if the user inputs 4.
# prints value is NOT 3 or 4 if the user enters any other integer.
# The sequence of operations begins on line 3, where we compare the user input against 3. If yes, line 4 runs; otherwise, we drop down to the else block.
# In the else block, we compare the input against 4 on line 6. If yes, line 7 runs; otherwise, we drop down to the inner else block and run the code on line 9.

# We recommend avoiding nested if statements when possible. They quickly become difficult to read with multiple levels of nesting or longish code blocks.
# However, don't get twisted up trying to avoid them entirely. Keep the nesting to a modest 2 or 3 levels deep and use functions to isolate some of the more complex code.

# You can rewrite the previous example using an elif block:

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')


# The elif block runs if value == 3 is False and value == 4 is True. The code produces the same results as the nested if.

# You can have as many elif blocks as you need, but they all need to be after the if block and, if the code has one, before the else block.
# The elif conditionals are evaluated in the order they appear in the code.

# Finally, if statement blocks may contain as many lines as you need:

if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')

# Every once in a while, you may want to create a block in an if statement that does nothing. We usually do this for readability purposes.
# However, blocks can't be empty. Instead, you have to use a pass statement.

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass  # We don't care about 9
else:
    print('value is something else')

# All statements in a block must be indented from the statement that begins the block. The indentation in a block must be consistent.
# If the first line of the block is indented 4 spaces, all statements in the block must be indented 4 spaces.

# Nested blocks should be indented more than the containing block.
# For instance, if the current block is indented by 4 spaces from the outer block (the conventional amount of indentation),
# then a nested block inside that block should be indented by 8 spaces. Another nested block would bring the indentation to 12 spaces.

# Be careful with your indentation. If you accidentally outdent some code, that will end the block. For instance:

if value == 1:
    print('value is one')
print('the value is odd')

# If you meant to print both messages when value is 1, that's what will happen. However, Python will display the second message even if value is not 1.
