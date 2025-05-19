operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    result = "Error! Division by zero."
    print(result)