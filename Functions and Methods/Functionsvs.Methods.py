# Methods provide the same benefits as functions. However, methods work with specific objects. All methods are functions but not vice versa.
# Every method belongs to a class and requires an object of that class to call it. For instance, in the following example,
# we're using the string object represented by my_str to call the upper method from the str class:

import math
my_str = 'abc-123-def'
print(my_str.upper())             # ABC-123-DEF

# Writing your own methods requires classes, which is how you create custom data types in Python. We're not ready to write our own classes and methods at this point;
# you'll learn how to do that in our Object Oriented Programming in Python book.

# In Python, the distinction between functions and methods may sometimes seem fuzzy. Some function invocations look like method invocations.
# For instance, consider the math module from Python's standard libraries. The module provides some mathematical functions that any program can use.
# Once you import the module, you just call the functions you need:


print(math.sqrt(5))             # 2.23606797749979

# Wait. Is that a method call? It sure looks like one. It quacks like one. Since math references an object, math.sqrt() must be a method call. However, it is not.
# While math is technically a reference to a module object, we're not using it to perform operations on that object.
# The sole purpose of the math object here is to tell Python where to look for those functions.

# For brevity, we often speak of functions when discussing functions and methods together.
# However, you should say methods when discussing functions explicitly designed to require calling objects.
