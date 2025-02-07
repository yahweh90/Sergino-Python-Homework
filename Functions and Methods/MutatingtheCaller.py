# Sometimes, a method mutates the object used to invoke the method: it mutates the caller.
# In the following example, the pop method mutates the caller (the list referenced by odd_numbers):

odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()
print(odd_numbers)  # [1, 3, 5, 7]

# We can also talk about whether functions mutate their arguments. The following function illustrates this concept:


def add_new_number(my_list):
    my_list.append(9)


numbers = [1, 2, 3, 4, 5]
add_new_number(numbers)
print(numbers)  # [1, 2, 3, 4, 5, 9]

# This code uses the list.append method to add a new number to the list my_list.Thus, list.append mutates its caller.
# However, the add_new_number function doesn't mutate a caller (there is no caller). Instead, it mutates its argument.

# In general, mutating the caller is acceptable practice; many built-in functions and methods do just that.
# However, you should avoid mutating arguments since such functions can be tough to debug and is considered poor practice.
# Almost no built-in functions mutate their arguments.

# Returning a new object


# def add_new_number(my_list):
#     return my_list + [9]


numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)
print(new_numbers)  # [1, 2, 3, 4, 5, 9]
print(numbers)     # [1, 2, 3, 4, 5]

# How do you know which methods mutate the caller and which don't? That's easy when the caller is immutable: the answer is always, "This method does not mutate the caller."
# However, when the caller is mutable, there's no way to say without inspecting the method's code or checking the documentation.
