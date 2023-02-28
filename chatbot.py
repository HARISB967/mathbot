def calculate(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            return "Can't divide by zero!"
        else:
            return num1 / num2
    else:
        return "Invalid operation!"


def display_menu():
    print("Available mathematical operations:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")


def main():
    while True:
        num1 = float(input("Enter the first operand: "))
        num2 = float(input("Enter the second operand: "))
        display_menu()
        operation = input("Enter the mathematical operation: ")
        result = calculate(num1, num2, operation)
        print("Result: ", result)
        choice = input("Do you want to perform another operation? (yes/no): ")
        if choice.lower() == "no":
            print("Thank you for using the bot!")
            break


main()
