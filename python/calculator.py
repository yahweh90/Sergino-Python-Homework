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
# Sergino-Python-Homework
