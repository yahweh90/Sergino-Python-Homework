# Consider this code:

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')


well_howdy('Angie')
print(greeting)

# In this code, we have a greeting variable in the body of well_howdy. When we call the function,
# Howdy is assigned to greeting, and a more complete greeting message is printed.

# When the function is done running, we try to print the value of the greeting variable. However, instead of seeing Howdy, we get an error message instead:

NameError: name 'greeting' is not defined

# The error occurs since the greeting variable is only available inside the well_howdy function. The surrounding code has no way to access the variable.

# What happens if we define our own greeting variable in the outer scope?

greeting = 'Salutations'


def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')


well_howdy('Angie')
print(greeting)

# This time, the code prints Salutations on line 8, thus showing that greeting is in scope on line 8.
# However, the outer greeting variable plays no part in the function's body. The assignment on line 4 hides the greeting variable from line 1.
# We call this variable shadowing.

# Let's remove the assignment on line 4 and see what happens:

greeting = 'Salutations'


def well_howdy(who):
    print(f'{greeting}, {who}')


well_howdy('Angie')
print(greeting)

# This time, we get:

Salutations, Angie
Salutations

# The key difference here is that we are no longer assigning the greeting variable in this function. Instead, we're just accessing its current value.
# It's the assignment in the first example in this section that causes Python to create a new local variable named greeting. Without any assignments in the function body,
# Python looks for greeting in the lexical scope, which means it searches the outer scopes for the nearest definition of greeting.
# In this example, the only outer scope of concern is the topmost scope, i.e., the global scope.

# If you're familiar with some other programming languages, the following example may be a little surprising:


def scope_test():
    if True:
        foo = 'Hello'
    else:
        bar = 'Goodbye'

    print(foo)
    print(bar)


scope_test()

Hello
UnboundLocalError: cannot access local variable
'bar' where it is not associated with a value

# In some languages, the corresponding print code may treat both foo and bar as out of scope. Both names may be in scope in other languages,
# but one will have a default value such as nil or undefined. In still other languages, only one name is in scope.
# Python comes closest to this last approach, but both names are technically in scope. However, since the else block never runs, bar is left unassigned.
# Thus, we get the UnboundLocalError message when we try to print it.

# As you might expect, constants have the same scoping behavior as variables. In fact, so do function, parameter, class, and module names.
# Method names act a little differently, but that's a topic for another time.
