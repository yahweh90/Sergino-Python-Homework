# Let's create an add function that returns the sum of two numbers:

def add(a, b):
    return a + b


add(2, 3)           # returns 5

# When you run this program, it doesn't print anything since add doesn't call print or any other output functions.
# However, the function does return a value: 5.
# When Python encounters the return statement, it evaluates the expression, terminates the function,
# then returns the expression's value to the location where we called add.

# Let's capture the return value in a variable and print it to verify that:


def add(a, b):
    return a + b


two_and_three = add(2, 3)
print(two_and_three)  # 5

# Python uses the return statement to return a value to the code that invoked the function. If you don't specify a value, it returns None.
# Either way, the return statement terminates the function and returns control to the calling function.

# Functions that always return a Boolean value, i.e., True or False, are called predicates. For example, the following function is a predicate:


def is_digit(char):
    if char >= '0' and char <= '9':
        return True

    return False
