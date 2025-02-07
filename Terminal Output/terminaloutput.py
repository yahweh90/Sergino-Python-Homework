# You've already seen one way to display output in the terminal: the print function.
# This built-in function takes any Python value, regardless of type, and prints it.
# Let's see an example. Create a file named greetings.py with the following content:

# name = 'Jane'
# print(f'Good morning, {name}!')

# In this simple example, we initialize a name variable with the string 'Jane', then use it in an f-string interpolation to build and display a greeting message.
# Run the program to see it in action:

$ python greetings.py
Good morning, Jane!

# The print() function works with all data types, often -- but not always -- formatting the output in some manner that makes it somewhat understandable to humans.
# For instance:

>> > print({'a': 1, "b": 42, 'c': "string",
            ...         'd': [5, 6], 'e': {8, 9, 10}})
# Pretty printed for clarity
{
    'a': 1,
    'b': 42,
    'c': 'string',
    'd': [5, 6],
    'e': {8, 9, 10}
}

>> > import time
>> > print(time.asctime())
Mon Aug 21 22: 59: 29 2023

# You can print multiple objects by just listing them one after the other as arguments to print():

>> > print(1, 2, 3, 'a', 'b')
1 2 3 a b


>> > print([1, 2, 3], 4, False, {5, 6, 7, 8})
[1, 2, 3] 4 False {8, 5, 6, 7}

# By default, multiple items are separated by spaces.
# You can use a different separator with the sep keyword argument (we discuss keyword arguments in the Core Curriculum):

print(1, 2, 3, 'a', 'b', sep=',')       # 1,2,3,a,b
print('a', 'b', 'c', 'd', 'e', sep='')  # abcde

Note that using an empty string as the sep value causes all the values to be printed without separation.

# The end keyword argument defines what print() prints after it prints the last argument. By default, it prints a newline (\n).
# The most common reasons for using end are compatibility with Windows (which sometimes needs a newline of \r\n) and for suppressing the newline altogether.
# Here are two more examples:

>> > print(1, 2, 'a', 'b', sep=',', end=' <-\n')
1, 2, a, b < -

>> > print('a', 'b', end='', sep=',')
print('c', 'd', sep=',')
a, bc, d

# Note the semicolon (;) on line 4: that's an easy way to enter multiple statements on a single line. Mostly, you should only use semicolons like this in the REPL.

# Finally, to start a new line immediately without printing anything else, just run print() with no arguments:

>> > print()

>> >
