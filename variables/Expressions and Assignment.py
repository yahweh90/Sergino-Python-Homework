# Assignment and reassignment are often more complex than simply assigning a literal value to a variable.
# Assignment and reassignment often use expressions on the right side of the = to determine the desired value. For instance:

left_side = 5
right_side = 32
total = left_side + right_side  # total = 37
print(total)                    # prints 37

# This code starts with two simple assignments that initialize the left_side and right_side variables to 5 and 32,
# respectively.
# Next, we add the values of left_side and right_side together and assign the result to total, which we then print.

# Here's an example that uses a function call to compute the resulting value for the assignment:


def square(number):
    return number * number


forty_two_squared = square(42)
print(forty_two_squared)              # 1764


# The expression on the right side of the = operator can be any valid expression.
# It can be as simple or complex as needed, though you should strive to keep them readable and easy to understand.

# The variable to the left of the = operator is always the target variable for the resulting value.
# That is, the expression's value will be assigned to the variable.

# It's worth noting that the right side of an assignment is always completely
# evaluated before assigning the result to the variable. That means you can write code like this:

foo = 42                    # foo is 42
foo = foo - 2               # foo is now 40
foo = foo * 3               # foo is now 120
foo = foo + 5               # foo is now 125
foo = foo // 25             # foo is now 5
foo = foo / 2               # foo is now 2.5
foo = foo**3                # foo is now 15.625
print(foo)                  # prints 15.625

# In lines 2-7, the right side of each assignment is computed first using whatever value foo had most recently.
# Thus, foo was 42 on line 2, 40 on line 3, and so on.
# On each line, a computation is performed using the current value of foo. Python then reassigns the newly computed value to foo.

# You can also use expressions to initialize constants. However, this is less common than evaluating expressions for a variable.
