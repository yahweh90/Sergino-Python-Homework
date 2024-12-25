# data type (int) Integer

import sys
1
2
-3
234891234
131_587_465_014_410_491

# Note that you can't use commas or periods for grouping: neither 123,456,789 nor 123.456.789 is valid.
# Instead, you can write the number without separators (123456789) or break up the number with underscores (123_456_789).
# There is no pre-defined limit to the size of an integer.
# You can have integers with as many digits as will fit in memory, though you may not be able to do much with them then.

############################## Floats #######################
# data type (float)

1.0
1.4142
-3.14159
42348.912346
131_587_465.014_410_491

# As with integers, you can't use commas or periods for grouping: neither 42,348,912.346 nor 42.348.912,346 is valid.
# Instead, you can write the number with only a single decimal point (42348.912346) or break up the number with underscores (42_348.912_346).

# Data Types (sys.float_info)


# The maximum number of digits that can be accurately
# presented
print(sys.float_info.dig)           # Typically 15

# The largest possible positive float value
print(sys.float_info.max)           # About 1.8 * (10**308)

# The smallest non-zero positive float value
print(sys.float_info.min)           # About 2.2 * (10**-308)

# Note that 10**n, where n is positive, represents a 1 followed by n zeros.
# Thus, 10**308 is a 1 followed by 308 zeros; a truly enormous number.
# On the other hand, 10**-n is equivalent to the reciprocal of 10**n, e.g., 1.0 / 10**n. Thus, 10**-308 is a truly minuscule number.

#### scientific notation ####

print(3.14 * (10**20))      # 3.14e+20
print(3.14 * (10**-20))     # 3.14e-20

# You can read the e+20 as meaning 10 to the 20th power, and e-20 as the reciprocal of 10 to the 20th power.

# You can also use scientific notation when writing float literals:
print(3.14e+20 / 2.72e-15)      # 1.1544117647058823e+35

# It's worth pointing out that these floating point issues are not present when working with integers.
# Integers can be as small or large as you want, provided they fit in memory. Furthermore, integers don't get printed with scientific notation.

print(3 * (10**20))             # 300000000000000000000
# If you want to use scientific notation to write a large integer, you must use the int function to convert the number to an integer:
print(int(3e+20))               # 300000000000000000000
