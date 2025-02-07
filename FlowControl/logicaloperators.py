# You're beginning to get a decent grasp of basic conditional flow. Let's take a few minutes to see how we can combine conditions to create more complex scenarios.
# The not, and, and or logical operators provide the ability to combine conditions:

# - not

# The not operator returns True when its operand is False and returns False when the operand is True. That is, it negates its operand.

print(not True)           # False
print(not False)          # True
print(not (4 == 4))         # False
print(not (4 != 4))        # True

# For completeness, let's see a few examples:

print((4 == 4) and (7 == 7))        # True
print((4 == 4) and (7 == 3))        # False
print((4 == 9) and (7 == 7))        # False
print((4 == 9) and (7 == 3))        # False


print((4 == 4) or (7 == 7))         # True
print((4 == 4) or (7 == 3))         # True
print((4 == 9) or (7 == 7))         # True
print((4 == 9) or (7 == 3))         # False

# As with not, parentheses aren't always needed. However, the same "precedence" issues may occur.
# Always use parentheses if the corresponding operand is not a literal or identifier.
