# The assignments at the end of the previous section all follow a similar pattern:
# they take the current value of a variable, perform an arithmetic operation on the variable's value, and then reassign the variable to the newly computed value.
# This sort of operation is so common that most languages have a shorthand notation called augmented assignment or assignment operators:

foo = 42              # foo is 42
foo -= 2              # foo is now 40
foo *= 3              # foo is now 120
foo += 5              # foo is now 125
foo //= 25            # foo is now 5
foo /= 2              # foo is now 2.5
foo **= 3             # foo is now 15.625
print(foo)            # prints 15.625

# Each statement is noticeably shorter than the original, but the results are identical.
# While there's little or no performance benefit to augmented assignment, most developers find the syntax more readable,
# and you're less likely to misspell one of the variable names.

# Augmented assignment also works with string concatenation and repetition. In fact, it works with any type that supports the various operators.

bar = 'xyz'           # bar is 'xyz'
bar += 'abc'          # bar is now 'xyzabc'
bar *= 2              # bar is now 'xyzabcxyzabc'
print(bar)            # prints xyzabcxyzabc

bar = [1, 2, 3]       # bar is [1, 2, 3]
bar += [4, 5]         # + with lists appends
# bar is now [1, 2, 3, 4, 5]
print(bar)            # prints [1, 2, 3, 4, 5]

bar = {1, 2, 3}       # bar is {1, 2, 3}
bar |= {2, 3, 4, 5}   # | performs set union
# bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}         # - performs set difference
# bar is now {1, 3, 5}
print(bar)            # prints {1, 3, 5}

# Augmented assignment also works with constants. However, as with constant reassignment, it is poor practice.

# Note that augmented assignment is a statement, not an expression. Thus, you can't use augmented assignment as a function argument or return value:


def foo(bar)


print(bar)


a = 3
foo(a *= 2)
#     ^^
# SyntaxError: invalid syntax


def foo():
    a = 3
    return a *= 2
#          ^^
#  SyntaxError: invalid syntax

# If you study the above examples, you may get the impression that a += b is equivalent to a = a + b.
# If the left-side variable (e.g., a) is immutable, that's true.
# However, if a is mutable, the expression may not be equivalent to a = a + b.
# For instance, if a and b are both lists, then a += b is actually equivalent to a.extend(b).
# The resulting values are the same, but we'll see later why this behavior is fundamentally different from a = a + b.
