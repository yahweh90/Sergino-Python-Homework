# Variables and Variable Names
# Consider this code:
answer = 41
print(answer)           # 41

answer = 42
print(answer)           # 42

# When Python sees line 1 of this code, it sets aside a bit of memory and stores the value 41 in that area.
# It also creates a variable named answer that we can use to access that value.

# On line 4, we reassign the value 42 to the variable named answer.
# That is, Python makes answer refer to a new object.
# In particular, you must understand that we're not changing the object that represents 41
# -- we're assigning an entirely new value to the answer variable.

# Variable Naming
# There are two hard problems in computer science: cache invalidation, naming things, and off-by-one errors.

# -- Author unknown

# Properly naming variables is traditionally viewed as one of the most challenging tasks in computer programming.
# If you're new to programming, this might seem odd.
# After all, how tough can it be to choose a name? As it turns out, it is challenging.
# Consider how much effort many new parents require to select a name for their baby.

# A variable name must accurately and concisely describe the variable's data.
# In large programs, it's challenging to remember what each variable contains.
# If you use non-descriptive names like x, i, and dct, you may forget what data that variable represents.
# Other readers -- programmers -- must suss out the meaning for themselves.
# Therefore, when naming variables, think hard about the names.
# Ensure they are accurate, descriptive, and understandable to other readers.
# That might be you when you revisit the program a few months or years later.

# Variable names are often referred to by the broader term identifiers.
# In Python, identifiers refer to several things:

# Variable and constant names
# Function and method names
# Function and method parameter names
# Class and module names
# You'll meet all these things as you move through the Launch School Core curriculum.
# We'll often use the term identifier when discussing names in general: variables, constants, functions, classes, etc.
# We'll use one of the more specific terms when we need to limit the scope of a discussion.
