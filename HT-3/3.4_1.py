# 3. Написати функцiю season, яка приймає один аргумент —
# номер мiсяця (вiд 1 до 12), яка буде повертати пору року,
# якiй цей мiсяць належить (зима, весна, лiто або осiнь)
def coffee_drinks():
    coffee_drinks = {'espresso': 20,
           'ristretto': 30,
           'americano': 35,
           'cappuccino': 40,
           'frappuccino': 40,
           'macchiato': 40,
           'mochaccino': 45
            }
    return coffee_drinks

def choose_drink():
    drinks = coffee_drinks()
    for key in drinks:
        print(key, '->',drinks[key], 'UAH')
    choice = input('\nEnter the drink from the list: ')
    return choice

def cups():
    cups = int(input('\nEnter the number of cups: '))
    print ('\nYou have chosen ', cups, 'cups')
    return cups

def buy_coffee_drinks():
    choice = choose_drink()
    order = cups()
    drinks = coffee_drinks()
    for drink,price in drinks.items():
        if choice == drink:
            total = price*order
            print('\nPay', total, 'UAH')
            payment = int(input('\nEnter the amount of money you insert: '))
            change = payment - total
            print('\nDon\'t forget to take your change: ', change, 'UAH')
