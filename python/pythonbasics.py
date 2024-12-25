# A Recursive Function - A function that calls itself
# def my_for(iterable):
#     if len(iterable) == 0:
#         return
#     print(iterable[0])
#     return my_for(iterable[1:])

# msg = "The Way of the Warrior is to know Death"
# my_for(msg)

# while answer = guess:
#     guess = int(input("Guess: "))

# msg = "The Way of the Warrior is to know Death"
# index = 0

#  print (msg[0])
#  print(msg[1])
#  ...
#  print(msg[2])
#  print(msg[26])
#
#  Iterate through msg
#  what do we need:
#     # length of msg
#     # an index
# print(len(msg))

# while index < len(msg):
#     print(msg[index])
#     # counter
#     # index = index + 1
#     index +=1

############# Build a Calculator ###################

# Exercise:
# fizz buzz
# if the input is divisible by 3 return "Fizz"
# if the input is divisible by 5 return "Buzz"
# if the input is divisible by both 3 and 5 it will return "FizzBuzz"
# for any other number it will return the same input
# Create a calculator that add, subtract, multiply and divide

def calculator():
    # get the first number
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator = input("What operation would you like to do? ")
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2


print(calculator())
