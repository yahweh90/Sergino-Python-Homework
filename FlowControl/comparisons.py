# The expressions to the left and right of an operator are its operands. For instance, the equality comparison x == y uses the == operator with two operands, x and y.
# ==

# The equality operator returns True when the operands have equal values, False otherwise. We discussed == briefly in the Basics Operations chapter.
# It should be familiar, even if it still looks strange.

print(5 == 5)                   # True
print(5 == 4)                   # False


print('abc' == 'abc')           # True
print('abc' == 'abcd')          # False


print(5 == 5)                   # False


print([1, 2, 3] == [1, 2, 3])   # True
print([1, 2, 3] == [3, 2, 1])   # False

# In most cases, operands must have the same type and value to be equal. Thus, 5 is not equal to '5'. There are some places where you can mix types, however.
# For instance, integers and floats that are mathematically equivalent are usually, but not always, considered equal:

print(5 == float(5))                  # True


big_num = 12345678901234567
print(float(big_num) == big_num)      # False

# Enormous floats lack precision at around 18 significant digits on most modern machines. That can lead to surprises if you happen to work with big numbers.

# Comparisons with strings are case-sensitive. Thus, 'abc' is not equal to 'aBc'.
# You can use the str.lower and str.upper methods to achieve a case-insensitive comparison:

print('abc' == 'aBc')                  # False
print('abc'.lower() == 'aBc'.lower())  # True
print('abc'.upper() == 'aBc'.upper())  # True

# In some non-US alphabets, converting text to upper or lower case isn't straightforward. For instance, in German, 'straße' and strasse are considered equivalent.
# However, the following code prints False:

'straße'.lower() == 'strasse'.lower()

# The str.casefold method makes allowances for this issue and does the right thing:

'straße'.casefold() == 'strasse'.casefold()

# While casefold is only needed when working with non-US characters, it's best practice in Python to use casefold instead of lower or upper,
# especially when comparing strings.

# !=

# The inequality operator, !=, is =='s inverse: It returns False when == would return True, and True when == would return False.
# It returns False when the operands have the same type and value, True otherwise. Other than the return value, the behaviors of == and != are identical.

print(5 != 5)             # False
print(5 != 4)             # True
print('abc' != 'aBc')     # False
print('abc' != 'aBc')     # True
print(5 != '5')           # True

# < and <=

# The less than operator (<) returns True when the value of the left operand has a value that is less than the value on the right, False otherwise.
# The less than or equal to operator (<=) is similar, but it also returns True when the values are equal; < returns False when the operands are equal.

print(4 < 5)              # True
print(5 < 4)              # False
print(5 < 5)              # False

print(4 <= 5)             # True
print(5 <= 4)             # False
print(5 <= 5)             # True

print('4' < '5')          # True
print('5' < '4')          # False
print('5' < '5')          # False

print('42' < '402')       # False
print('42' < '420')       # True
print('420' < '42')       # False


# The examples with strings are especially tricky here! Make sure you understand them. Python compares strings character-by-character, moving from left to right.
# It looks for the first character that differs from its counterpart in the other string.
# Once it finds differing characters, it compares them to determine the relationship.

# If both strings are equal up to the shorter string's length, as in the last two examples, the shorter one is considered less than the longer one.

# > and >=

# The greater than operator (>) returns True when the value of the left operand has a value that is greater than the value on the right, False otherwise.
# The greater than or equal to operator (>=) is similar, but it also returns True when the values are equal; > returns False when the operands are equal.

print(4 > 5)              # False
print(5 > 4)              # True
print(5 > 5)              # False


print(4 >= 5)             # False
print(5 >= 4)             # True
print(5 >= 5)             # True


print('4' > '5')          # False
print('5' > '4')          # True
print('5' > '5')          # False


print('42' > '402')       # True
print('42' > '420')       # False
print('420' > '42')       # True

# As with < and <=, you can compare strings with the > and >= operators; the rules are similar.
