def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def should_continue(result):
    decission = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
    if decission == 'y':
        return True
    elif decission == 'n':
        return False
    else:
        print("Wrong input!")

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

result = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")

continue_calculation = should_continue(result)

while continue_calculation:
    operation_symbol = input("Pick next operation: ")
    num1 = result
    num2 = int(input("What's the next number?: "))
    result = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    continue_calculation = should_continue(result)

