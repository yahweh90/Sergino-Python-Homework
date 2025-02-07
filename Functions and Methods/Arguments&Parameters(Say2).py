# Create a new file named say2.py with the following code:

print('hello')
print('hi')
print('how do you do')
print('Quite all right')

# Go ahead and run it if you want. Notice how we've duplicated the print call several times. Instead of calling it every time we want to output something,
# we want to have code we can call when we need to print something.

# Now, let's update say2.py as follows:


def say(text):
    print(text)


say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# You can define functions that take any number of parameters and accept any number of arguments.
# For instance, the add function defined below takes two parameters, and we invoke it with 2 arguments:


def add(left, right):
    sum = left + right
    return sum


sum = add(3, 6)

# In the above code, left and right are parameters on line 1. On line 2, however, they are local variables that contain the argument values passed to add on line 5.

# Python will raise an error if you pass too many or too few arguments to a function. However, it is possible to bypass this restriction, as we'll see later.

# Let's return to say2.py. When we called say('hello'), we passed the string 'hello' as the argument. Thus, 'hello' was assigned to the text parameter.

# As mentioned earlier, one benefit that functions give us is the ability to make changes in one location.
# Suppose we want to add a ==> to the beginning of every line that say outputs.
# All we have to do is change one line of code -- we don't have to change the function invocations:


def say(text):
    print('==> ' + text)


say('hello')        # ==> hello
say('hi')           # ==> hi
say('how are you')  # ==> how are you
say("I'm fine")     # ==> I'm fine

# Run this code to see the result. We've now added a ==> to the beginning of each line. We only had to change a single line of code.
# Now, you're starting to see the power of functions.
