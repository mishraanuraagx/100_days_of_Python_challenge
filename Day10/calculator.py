def add(a: float, b: float):
    return a + b


def sub(a: float, b: float):
    return a - b


def mul(a: float, b: float):
    return a * b


def div(a: float, b: float):
    if b != 0.0:
        return a / b
    else:
        raise Exception("Divide by zero not allowed.")


def main():
    operations = ["+", "-", "/", "*"]
    print(calculator_logo)
    print(calculator_logo2)
    print(f"All possible operations: {operations}")
    continue_process = True
    a: float = None
    b: float = None

    action = input("What operation would you like for us to perform: ")
    while continue_process:
        if action not in operations:
            raise Exception("Invalid Operations.")
        if a == None:
            a = float(input("Enter a number: "))
        if b == None:
            b = float(input("Enter another number: "))
        result = perform_action(a, b, action)
        print(f"Output of {a} {action} {b} = {result}\n")

        a = result
        # Unset B
        b = None
        action = input("Do you wish to conitnue execution. Enter the next operation.")
        if action == "":
            continue_process = False



def perform_action(a: float, b: float, action):
    if action == "+":
        return add(a, b)
    if action == "-":
        return sub(a, b)
    if action == "*":
        return mul(a, b)
    if action == "/":
        return div(a, b)


calculator_logo = '''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              '''

calculator_logo2 = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

if __name__ == "__main__":
    main()
