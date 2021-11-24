# Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя
# яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator():
    x = float(input("Enter the 1st number: "))
    while True:
        operation = input('Enter the operation: ')
        y = float(input("Enter the 2nd number: "))
        if operation == '+':
            x = x + y
            print('Result is:', x)
        elif operation == '-':
            x = x - y
            print('Result is:', x)
        elif operation == '/':
            if y == 0:
                print ('Null division. Error.')
                y = float(input("Enter another number: "))
                x = x / y
                print('Result is:', x)
            else:
                x = x / y
                print('Result is:', x)
        elif operation == '*':
            x = x * y
            print('Result is:', x)

calculator()
    
