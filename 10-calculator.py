# let's use what we've learned to make a basic calculator function

def calculate(a, operation, b):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        return a / b

while True:
    a = int(input("a: "))
    operation = input("operation: ")
    b = int(input("b: "))
    result = calculate(a, operation, b)
    print(a, operation, b, "=", result)
    print()