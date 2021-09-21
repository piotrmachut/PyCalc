from ascii import logo
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def should_continue(result):
    decission = input(f"Type 'y' to continue calculating with {result}, or type 'n' start new calculation: ")
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

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        check = should_continue(result)

        if check:
            num1 = result
        elif not check:
            continue_calculation = False
            clear()
            calculator()

calculator()