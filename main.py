def calculator():
    bool = 1
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter 2nd Number: "))
    while bool == 1:
        operator = str(input("Enter operator: '+' '-' '/' '*': "))
        if operator == '+':
            result = num1 + num2
            print(result)
            break
        elif operator == '-':
            result = num1 - num2
            print(result)
            break
        elif operator == '/':
            result = num1 / num2
            print(result)
            break
        elif operator == '*':
            result = num1 * num2
            print(result)
            break
        elif operator != '+' or '/' or '-' or '*':
            print("Wrong OPERATOR")


def maincal():
    print("Welcome to the calculator")
    print("-------------------------")
    calculator()
    choice = (input("Do you want to continue? Y/N "))
    if choice == 'Y' or choice == 'y':
        calculator()


maincal()
