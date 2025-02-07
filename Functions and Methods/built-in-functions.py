# min and max
# You can use the min and max functions to determine a collection's minimum and maximum values.
# The collection's objects must have an ordering that recognizes the < and > operators for comparing any pair of those objects.

print(min(-10, 5, 12, 0, -20))        # -20
print(max(-10, 5, 12, 0, -20))        # 12


print(min('over', 'the', 'moon'))     # 'moon'
print(max('over', 'the', 'moon'))     # 'the'


print(max(-10, '5', '12', '0', -20))
# TypeError: '>' not supported between instances
# of 'str' and 'int'

# You can also use max and min with a single iterable argument, such as a list, set, or tuple:

my_tuple = ('i', 'tawt', 'i', 'taw', 'a',
            'puddy', 'tat')
print(min(my_tuple))  # 'a'
print(max(my_tuple))  # 'tawt'

# For now, you only need to know that strings, sequences, mappings, and sets are iterable.

# ord and chr
# Given a single character, ord returns an integer that represents the Unicode code point of that character.
# For the standard ASCII character sets, the code points refer to the values of the characters in the standard ASCII character set. For example:

print(ord('a'))                     # 97
print(ord('A'))                     # 65
print(ord('='))                     # 61
print(ord('~'))                     # 126

# chr is the inverse of ord. That is, it converts an integer to the corresponding Unicode character:

print(chr(97))          # a
print(chr(65))          # A
print(chr(61))          # =
print(chr(126))         # ~
