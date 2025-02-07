# Unless a function is built-in or provided by an imported module, you must create it. A typical function definition (a.k.a., function declaration) looks like this:

def func_name():
    func_body

# Here, we're assigning the function to func_name, and func_body is some code that performs the function's required action(s).

# Here's a function named say that prints Hi!:


def say():
    print('Hi!')

# Why do we want a function named say? To say something, of course! Let's try it. First, we'll create a file named say.py, then place the following code inside the file.


def say():
    print('Output from say')


print('First')
say()
print('Last')

# Save the file and run it from the terminal:

$ python say.py
First
Output from say
Last

# On line 5 of say.py, the code say() is a function call to the say function. When Python runs this program, it creates a function named say whose body causes Python
# to print the text Output from say when the function executes. However, that doesn't happen immediately.

# On line 4, we use print to display First on the terminal. On line 5, we call the function say by appending a pair of parentheses -- () -- to the function's name.
# This causes Python to temporarily jump into the function's body, which prints the text Output from say. Finally, Python returns to the code
# that immediately follows the call to say and prints Last.

# Note that the parentheses on line 5 -- () -- make this code a function call. Without the parentheses, say doesn't do anything useful.
# It's the function's name, not an invocation. Forgetting the parentheses is usually a bug that can be tough to find since the code may run long after the
# line with the error. It just won't work. We'll learn about function objects later in the Core Curriculum.

# Python programmers often add a triple-quoted string at the beginning of a function's block. This string is a documentation comment -- a docstring -- that Python
# can access with its help() function and the __doc__ property. It has no effect on your code unless your program is somehow interested in the comments (which can happen):


def say():
    """

    The say function prints "Hi!"
    """

    print('Hi!')


print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)

------------------------------------------------------------------------------------------------

      The say function prints "Hi!"


------------------------------------------------------------------------------------------------
Help on function say in module \_\_main\_\_:


say()
    The say function prints "Hi!"
    
