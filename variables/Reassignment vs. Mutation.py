# Here are some examples illustrating the differences between reassignment and mutation. Pay close attention, as this is a crucial concept.

num = 3               # assignment (initialization)
my_list = [1, 2, 3]   # assignment (initialization)
my_dict = {           # assignment (initialization)
    'a': 1,
    'b': 2,
}


num = 42              # Reassignment
my_list[1] = 42       # Reassignment of element,
# my_list is mutated!
my_dict['b'] = 3      # Reassignment of dict pair
# my_dict is mutated!


# You can still reassign the variables
my_list = [2, 3, 4]   # Reassignment
my_dict = {'x': 0}   # Reassignment

# Things get a little fuzzy when using augmented assignment. As mentioned earlier, a += b is equivalent to a = a + b if a is immutable.
# In that case, then augmented assignment is a form of reassignment.

# However, if a is mutable, it may be (and frequently is) mutated in augmented assignments.
# As we mentioned earlier, a += b is equivalent to a.extend(b) if a and b are lists. Thus, a += b is not reassignment; it is a mutating operation.
# This distinction becomes crucial when we discuss variables as pointers.
