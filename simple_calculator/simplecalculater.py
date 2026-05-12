def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

operation_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print("Welcome to simple calculator")
    num_1 = int(input("Enter the first number: "))
    for symbol in operation_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        select_operation = input("Enter the operation: ")
        num_2 = int(input("Enter the second number: "))
        calculator_function = operation_dict[select_operation]
        result = calculator_function(num_1, num_2)
        print(f"{num_1} {select_operation} {num_2} = {result}")

        should_continue = input(f"press 'y' to continue calculation with {result} or 'n' to calculate new calculation or 'x' to exit: ").lower()
        if should_continue == 'y':
            num_1 = result
        elif should_continue == 'n':
            continue_flag = False
            calculator()
        else:
            continue_flag = False
            print("Bye...😊")
calculator()

