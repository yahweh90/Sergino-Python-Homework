# To invoke a function, write the function's name followed by a pair of parentheses ().
# For example, when we call the hello function in the following code, we write hello():

def hello():
    print('Hello')
    return True


hello()           # invoking function; ignore return value
print(hello())    # using return value in a `print` call

# The first 3 lines of this program contain the function definition or function declaration. We'll come back to function definitions a little later in this chapter.
# For now, notice that the function returns the value True when it is done running.

# Lines 5 and 6 show two calls to the hello function. In the first invocation, we ignore the return value.
# In the second, we capture the return value and pass it to the print function for printing.

# What does the print function return? That's easy to check:

> > > print(print())
None

# We'll see why that is later.

# Functions can also take one or more comma-separated arguments between the parentheses. Functions usually use arguments to modify the actions they take.
# A single argument is passed to the print function on lines 2 and 6 above. In this case, it tells print what to print.

# To provide additional arguments, separate them with commas:

print('hello', 'good-bye', 'farewell')

# If you have a lot of arguments (or some longish ones), you can spread them over several lines:

print(
    'hello',
    'good-bye',
    'farewell',
    'adios',
    'ciao',
    'auf wiedersehen',
)
