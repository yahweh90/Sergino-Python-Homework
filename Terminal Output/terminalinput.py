# Example: Greet the User By Name
# Let's use input() to write a program that displays a personalized greeting message for the user based on the name she provides.
# Create a file named personalized_greeting.py with the following code:

print("What's your name?")
name = input()


print(f'Good Morning, {name}!')

# Run the program from the command line. It displays the What's your name? question, then waits for your input.
# When you enter a name and hit Return, the program displays a custom greeting message:

$ python personalized_greeting.py
What's your name?
Rachele
Good Morning, Rachele!

# You can also use the input() function to display the prompt the user sees:

name = input("What's your name? ")

print(f'Good Morning, {name}!')

# Note the space after the ?: you'll see why that's needed when you run the program:

$ python personalized_greeting.py
What's your name? Rachele
Good Morning, Rachele!

# See how input() retrieved the input from the same line as the prompt? That's why we needed the extra space. Without the space, we'd see:

What's your name?Rachele
Good Morning, Rachele!

# Alternatively, we can have input() output a newline instead of a space:

name = input("What's your name?\n")

print(f'Good Morning, {name}!')

$ python personalized_greeting.py
What's your name?
Rachele
Good Morning, Rachele!

# That's more like what we started with when we used print() to display the prompt. In this code, the \n is an escape character that the computer treats as a newline. 
# \n is accepted almost universally in programming languages, though the circumstances needed to produce the desired effect may vary slightly.

# Add Two Numbers
# Let's write a program that asks for two numbers from the user, adds them, and then displays the result. 
# Put the following code in a new file called sum_numbers.py and then run it:

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = number1 + number2

print(f'The numbers {number1} and {number2} '
      f'add to {sum}')

$ python sum_numbers.py
Enter the first number: 2
Enter the second number: 3
The numbers 2 and 3 add to 23

# Oops. Something isn't right. The program reports that the result is 23, not 5 like we want. 
# Where do you think the problem lies? If you said that input() returns strings, so + performs concatenation, 
# you're right! Since number1 and number2 both hold string values instead of numbers, the + operator concatenates them instead of adding them. 
# If you want to add two variables arithmetically, both must have a numeric data type.

# As we learned earlier, we can convert (coerce) strings to numbers with the int() or float() function. Update line 3 from sum_numbers.py to match this code:

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f'The numbers {number1} and {number2} add to {sum}')

$ python sum_numbers.py
Enter the first number: 2
Enter the second number: 3
The numbers 2 and 3 add to 5.0

# input() still returns a string, but we've coerced each string to a float this time. With numbers on both sides of the +, Python adds them arithmetically.

# Be sure to play with these examples a bit. You can, for example, replace addition with subtraction or multiplication in the above example. 
# Try to think of some applications of input() on your own.

# I/O (Input/Output) in Python is a complex topic requiring knowledge of concepts we haven't yet learned. 
# They're essential concepts, but we don't discuss them in this book; we cover them in the Core Curriculum. 
# Until then, we can use print() and input() to interact with users.