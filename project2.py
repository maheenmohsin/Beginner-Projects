#Project2: Simple Calculator Project

print("Welcome to python simple calculator")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operation = input("Choose operation(+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalis Operation! Please choose +, -, * or /.")