# It's sometimes helpful to invoke a function without some of its arguments. You can do that by providing default values for the function's parameters.
# Let's update say to use a default value when the caller omits the argument.

def say(text='hello'):
    print(text + '!')


say('Howdy')  # Howdy!
say()         # hello!

# Notice that invoking say without arguments, as on line 5, prints 'hello!'. We can invoke say without arguments since we've provided a default value for text. Nice!

# You can provide defaults for any or all of a function's parameters. However, once you specify a default value for a parameter,
# all subsequent positional parameters must also have default values:


def say(msg1, msg2, msg3='dummy message', msg4):
    pass
# SyntaxError: non-default argument follows default argument

# It's also worth noting that you can't accept the default value for a parameter and provide an explicit value for a subsequent parameter:


def say(msg1, msg2, msg3='dummy message',
        msg4='omitted message'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)


say('a', 'b', 'c', 'd')
# a
# b
# c
# d

say('a', 'b', 'c')
# a
# b
# c
# omitted message

say('a', 'b', , 'd')
# a
# b
# d               # oops - expecting 'dummy message'
# omitted message # oops again - expected 'd'

# Python has a variety of ways to specify parameters. The easiest is with positional parameters.
# With positional parameters, the parameter values are taken from the corresponding argument position.
# Thus, if you have a function that takes 3 parameters, the first parameter is set to the first argument,
# the second parameter to the second argument, and the third parameter to the third argument.
# For instance, in the say function above, the 4 parameters are assigned based on the order of the arguments.
# Of course, default parameters mean you can omit some arguments.
