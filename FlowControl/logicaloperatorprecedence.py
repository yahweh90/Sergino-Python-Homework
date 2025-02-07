# Even though and has higher precedence than or, the fact that both are short-circuiting operators adds a whole lot of complexity.
# For example, can you determine what the following code prints?

print(1 or 2 and 3)
print(0 or 2 and 3)
print(1 or 0 and 3)
print(1 or 2 and 0)
print(0 or 0 and 3)
print(0 or 2 and 0)
print(1 or 0 and 0)
print(0 or 0 and 0)

print(1 and 2 or 3)
print(0 and 2 or 3)
print(1 and 0 or 3)
print(1 and 2 or 0)
print(0 and 0 or 3)
print(0 and 2 or 0)
print(1 and 0 or 0)
print(0 and 0 or 0)

# Go ahead and guess what will be output, then try running the code to see the results. In all likelihood, you will guess incorrectly at least once.

# We're not going to try to explain what's happening with this code.
# While you might encounter some code like this in the future, the mixed and/or code will likely only be a small part of your problems.

# In short: do not write code like this! If you must mix and and or, use parentheses to control how the code gets written. For instance, compare these two lines of code:

print((a and b) or (c and d))
print(a and b or c and d)

# The first line, while complex, is easier to understand than the second.

# To repeat, avoid mixing and and or in a single expression unless you use parentheses to control the order of evaluation.
