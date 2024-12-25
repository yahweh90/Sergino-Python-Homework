################## Escape Sequences#################
message = 'Python "Programming'
#   \"
#   \'
#   \\
#   \n

message = "Python \nProgramming"
# -----------------OR--------------#
# ---------------- Using this code creates a missing line ----------------#
message = """
Python
Programming
"""
# ------------------OR----------------#
# ------------------For filling in the missing line ---------------#
message = """Python
Programming
"""
print(message)
