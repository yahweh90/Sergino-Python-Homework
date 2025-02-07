# We create (initialize) most variables by simply giving them a value.
# That happens as part of an assignment statement:

forename = 'Clare'        # initialization (also called assignment)

# Initializations are also said to provide a definition for the variable.

# No special keywords are required to define variables.
# We can also give new values to variables by simply reassigning them:

forename = 'Clare'        # initialization (also called assignment)
# omitted code
forename = 'Victor'       # reassignment

# How Initialization and Reassignment Work
# When you initialize a variable, Python gives it an initial value and sticks
# that value somewhere in the computer's memory.
# It also allocates a small amount of memory for the variable itself,
# then places the value's memory address into the variable's spot in memory.

# For instance, consider this code:

foo = 'abcdefghi'

# Consider what happens when we later run this reassignment:

foo = 'Hello'
