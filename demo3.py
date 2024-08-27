def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")
    print("-----------------")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    if choice in operations:
        result = operations[choice](num1, num2)
        operation_symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
        print(f"\n{num1} {operation_symbols[choice]} {num2} = {result}")
    else:
        print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()
