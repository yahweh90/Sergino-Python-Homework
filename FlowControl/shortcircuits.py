# The and and or operators use a mechanism called short circuit evaluation to evaluate their operands. Consider these two expressions:

is_red(item) and is_portable(item)
is_green(item) or has_wheels(item)

# The first expression returns True when item is red and portable. If either condition is False, then the overall result must be False.
# Thus, if the program determines that item is not red, it doesn't have to determine whether it is also portable.
# Python short-circuits the rest of the expression by terminating evaluation if it determines that item isn't red.
# It doesn't need to call is_portable() since it already knows the expression must be False.

# Similarly, the second expression returns True when item is either green or has wheels. When either condition is True, the overall result must be True.
# Thus, if the program determines that item is green, it doesn't have to decide whether it has wheels.
# Again, Python short-circuits the entire expression once it knows that item is green; the expression must be True.
