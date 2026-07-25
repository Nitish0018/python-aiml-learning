def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation."

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Function call
result = calculator(a, b, operation)
print("Result:", result)