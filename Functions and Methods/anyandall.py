# any and all
# The any function returns True if any element in a collection is truthy, False if all of the elements are falsy.
# On the other hand, all returns True if all of the elements are truthy, False otherwise.

collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))       # False
print(any(collection2))       # True
print(any(collection3))       # True
print(any([]))                # False

print(all(collection1))       # False
print(all(collection2))       # False
print(all(collection3))       # True
print(all([]))                # True

# Notice that any returns False for an empty collection since none of the elements are truthy.
# However, all returns True for the same collection since none of the elements are falsy (all of the elements are thus truthy).

# This example may not seem very useful. However, if you have a collection of something other than Booleans,
# you can use a comprehension with any or all to test whether any or all of the elements meet a certain condition. (We'll meet comprehensions a little later.)

# For instance, assume you want to determine whether a list of numbers has any even values in it.
# You can use a list comprehension to determine which values are even or odd:

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for numbetr in numbers])
# [True False True True False]

# You can take that one step further to determine whether any or all of the numbers are even:

numbers = [2, 5, 8, 10, 13]
print(any([number % 2 == 0 for number in numbers]))  # True
print(all([number % 2 == 0 for number in numbers]))  # False

numbers = [5, 13]
print(any([number % 2 == 0 for number in numbers]))  # False
print(all([number % 2 == 0 for number in numbers]))  # False

numbers = [2, 8, 10]
print(any([number % 2 == 0 for number in numbers]))  # True
print(all([number % 2 == 0 for number in numbers]))  # True

# Functions for the REPL
# Some functions are intended for use in a REPL. These functions provide quick access to information about your program or Python itself.

# The id Function
# The id function returns an integer that serves as an object's identity. Every object has a unique identity that does not change during the object's lifetime.
# (The identity may be reused later in the program if the original object is discarded.)

# In most cases, two instances of an object with the same value will always have two distinct identities.
# This is not always true, though. For instance, in a process called interning, every unique integer object from -5 through 256 has the same identity.
# Interning also applies to some strings:

# paste this code into the Python REPL
# Don't run it as a program

s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

x = 5
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False

Interning yields memory space savings and performance improvements.
We discuss it mainly because new Python programmers sometimes discover this behavior and think they've found a bug. In practice, it's not an important concept,
but it's worth being aware of.

By the way: the reason we asked you to paste that code into the Python REPL is that Python interns different things when you run a program file. 
In the above code, the first print will output True if you run it as a program.

Later on, we'll see why id is useful.

Interning is an implementation detail that varies based on the flavor and version of Python you are using. 
While most flavors and versions intern the small integers shown above, some intern other values such as certain strings.

Python "flavors" are different implementations of Python. 
The flavor you are most likely using is CPython, but other flavors include Jython, PyPy, AnacondaPython, and more.

# The dir Function

>>> dir()
['__builtins__', '__name__', 'struct']

>>> dir(5)
['__abs__', '__add__', '__and__', '__bool__',
    ... a bunch of stuff omitted ...,
    '__xor__', 'as_integer_ratio', 'bit_count',
    'bit_length', 'conjugate', 'denominator',
    'from_bytes', 'imag', 'numerator', 'real',
    'to_bytes']

# Helpful Hint: Use the sorted function with the output of dir:

>>> sorted(dir(range(1)))
['__bool__', '__class__', '__contains__',
 '__delattr__', '__dir__', '__doc__', '__eq__',
    ... a bunch of stuff omitted ...
    'count', 'index', 'start', 'step', 'stop']

# Another Helpful Hint: Use pretty print to print the output in an easier to read format:
>>> from pprint import property
>>> names = sorted(dir(range(1)))
>>> pp(names)
['__bool__',
 '__class__',
 '__contains__',
 '__delattr__',
 ... a bunch of stuff omitted ...,
 'count',
 'index',
 'start',
 'step',
 'stop']

# Yet Another Helpful Hint: Use a comprehension to limit the output to just the names that don't contain __.

>>> names = sorted(dir(range(1)))
>>> names = [name for name in names
...           if '__' not in name]
>>> print(names)
['count', 'index', 'start', 'step', 'stop']

# The help Function
# When used without arguments, the help function prints some basic help on how to use help, then leaves you in a special help mode that uses a help> prompt.

>>> help()

Welcome to Python 3.11's help utility!

if this is your first time using Python, you should definitely check out the tutorial on the internet at https://docs.python.org/3.11/tutorial/.

Enter the name ...
    <omitted text>
    
help>

# From the help> prompt, you can request help on module names, Python keywords, built-in functions, class names, etc. 
# Type the appropriate words at the help> prompt and press {Return} or {Enter}.

# Quitting the help system may involve two separate steps. If you are currently reading a long help item (such as the help for str), 
# you may need to press q to terminate the output. After terminating the output, 
# you may need to type another q and then press {Return} or {Enter} to exit from the help> prompt.

# As of Python 3.13.0, you no longer need to use write help() to access the help system. You can, instead, just write help. 
# When supplying an argument to help, you still need to use the parentheses.

# You can also request help more directly by placing an appropriate identifier between the parentheses:

>>> help(ord)
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

>>> help(bool)
Help on class bool in module builtins:

class bool(int)
 |   bool(x) -> bool
 |
 |   Returns True when the argument x is true, False otherwise.
 |   The builtins True and False are the only two instances of the class bool.
 |   The class bool is a subclass of the class int, and cannot be subclassed.
 |
 |   Method resolution order:
 |   bool
 |   int
 |   object
 
  <omitted text>
  
>>> help('topics')

Here is a list of available topics. Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING         SHIFTING

ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS  SLICINGS

ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS        SPECIALATTRIBUTES

ATTRIBUTES          DYNAMICFEATURES     METHODS         SPECIALIDENTIFIERS

AUGMENTEDASSIGNMENT Ellipsis            MODULES         SPECIALMETHODS
   <omitted text>
   
>>> help('BOOLEAN')
Boolean operations
******************


   or_test   ::= and_test | or_test "or" and_test
   and_test  ::= not_test | and_test "and" not_test
   not_test  ::= comparison | "not" not_test
   
In the context of Boolean operations, and also when expressions are
used by control flow statements...

   <omitted text>