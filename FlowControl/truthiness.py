# Enough yammering. Let's see some examples:

value = 5               # 5 is truthy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')


value = 0               # 0 is falsy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')

# The first example prints 5 is truthy while the second prints 0 is falsy. This works since Python evaluates 5 as truthy and 0 as falsy.

# You may sometimes see articles that speak of true and false values; this even happens in the Python documentation.
# The authors should probably talk of truthy and falsy evaluations, instead, not true and false.
# At Launch School, we want you to use truthy and falsy when speaking of truthiness, True and False when talking of booleans,
# and true and false when discussing truths and falsehoods.

# You may have noticed how we took care to say things like evaluates as truthy. For brevity, you can simply describe expressions as either truthy or falsy.
# The "evaluates as" terminology is unnecessary.

#####################################################################################################

# Truthiness and Short-Circuit Evaluation

# You may recall that the and and or logical operators cause short-circuit evaluation. You may not realize that the logical operators don't always return True or False.
# Both operators care only about the truthiness of their operands.
# The final value returned by an expression using and and or is the value of the final sub-expression evaluated by Python:

print(3 and 'foo')    # last evaluated op: 'foo'
print('foo' and 3)    # last evaluated op: 3
print(0 and 'foo')    # last evaluated op: 0
print('foo' and 0)    # last evaluated op: 0

print(3 or 'foo')     # last evaluated op: 3
print('foo' or 3)     # last evaluated op: 'foo'
print(0 or 'foo')     # last evaluated op: 'foo'
print('foo' or 0)     # last evaluated op: 'foo'
print('' or 0)        # last evaluated op: 0
print(None or [])     # last evaluated op: []

# Suppose you have a logical expression that returns a non-Boolean object instead of a Boolean:

foo = None
bar = 'qux'
is_ok = foo or bar

# In this code, is_ok gets set to the truthy value, 'qux'. In most cases, you can use 'qux' as though it were a Boolean True value.
# However, using a string as a Boolean isn't always the best way to write your code. It may even look like a mistake to another programmer trying to track down a bug.
# In some strange cases, it may even be a mistake.

# You can readily address this with an if/else statement:

if foo or bar:
    is_ok = True
else:
    is_ok = False

# This snippet sets is_ok to either True or False based on the truthiness of foo or bar. However, it is wordy.
# Many Python programmers would write this more concisely as:

is_ok = bool(foo or bar)
