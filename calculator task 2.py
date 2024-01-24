def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return None


num1 = float(input("Enter the  first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation you wanna perform (+,-,*,/): ")

result = calculator(num1, num2, operation)
if result is not None:
    print("Result: ", result)
else:
    print("Invalid operation")
