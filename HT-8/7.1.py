import json
import pprint
import sys

'''
Username:
- 3-25 symbols,
- only letters
- 1st uppercase, else lowercase

Password:
- 4 symbols
- only digits

Incasator:
Admin1': 1111,
Admin2': 2222
'''

counter = 0
trials = 3
while counter < 3:
    username = input('Please, enter your username: ').rstrip()
    password = input('Please, enter your password: ')
    counter += 1
    trials -= 1
    if counter == 3:
        print('No trials left.')
        break
    else:
        if trials == 1:
            print('Only', trials, 'trial left.')
        elif username.isalpha() != True:
            print('The username must consist of only alphabetical characters')
            print('Only', trials, 'trials left.')
        elif password.isdigit() != True:
            print('The password must include only digits.')
            print('Only', trials, 'trials left.')
        elif len(username)<3 or len(username)>25:
            print('The username must be more than 3 and less than 25 symbols')
            print('Only', trials, 'trials left.')
        elif len(password) != 4:
            print('The password must consist of 4 numbers.')
            print('Only', trials, 'trials left.')
        elif username[0].isupper() != True:
            print('The first letter of the username must be upper case')
            print('Only', trials, 'trials left.')
        elif username[1:].islower() != True:
            print('Only the first letter of the username must be upper case')
            print('Only', trials, 'trials left.')
        else:
            break
password = int(password)

class LoginException(Exception):
    pass

class NumberException(Exception):
    pass

def login_menu():
    login_menu = {
                'Authotization': 1,
                'Registration': 2,
                'Incasator': 3
                 }
    return login_menu

def menu1():

    def incasator():

        incasator_operations()
        incasator_mode()

    def balance_file():

        balance = {'balance:': 0}
        with open(username + '_balance.data.json', 'w') as balance_f:
            json.dump(balance, balance_f, indent=2, ensure_ascii=False)
        return balance

    def transactions_file():

        transaction = {username: 0}
        with open(username + '_transactions.json', 'w') as transactions_f:
            json.dump(transaction, transactions_f, indent=2, ensure_ascii=False)
        return transaction

    def registration():

        try:
            with open('users.data.json') as file:
                users_data = json.load(file)
        except:
            users_data = {}

        user = {username: password}
        user_i = user.items()
        users_data_i = users_data.items()
        if user_i & users_data_i != user_i:
            users_data.update(user)
            with open('users.data.json', 'w') as file:
                json.dump(users_data, file, indent=2, ensure_ascii=False)
                balance_file()
                transactions_file()
                print('Congratulations! You\'ve got your personal card :)')
        else:
            print('Your account already exists.')

        return users_data

    def authorization():

        print('Hello!')
        user = {username: password}
        with open('users.data.json') as file:
            users_data = json.load(file)
        user_i = user.items()
        users_data_i = users_data.items()

        for k,v in user_i:
            if user_i & users_data_i == user_i:
                print('Please, choose the operation: ')
            else:
                print('Sorry, there is no such client. I register you in a bank system.')
                registration()
        return user

    menu1_switch = {
                    1: authorization,
                    2: registration,
                    3: incasator
                    }

    menu1 = login_menu()
    print('Welcome! Choose the SignUP or LogIn operation: ')
    for key in menu1:
        print(key, '->', menu1[key])
    choice1 = int(input('Enter the number of your choice: '))
    output1 = menu1_switch.get(choice1)()

    return

def operations_menu():

    operations_menu = {
                'Cash payment': 1,
                'Withdraw money': 2,
                'View balance': 3,
                'View transaction history': 4,
                }
    return operations_menu

def menu2():

    def view_balance():

        with open(username + '_balance.data.json', 'r') as balance_f:
            balance_data = json.load(balance_f)
            for k,balance in balance_data.items():
                print('Your current', k, balance)

    def view_transaction_history():

        with open(username + '_transactions.json', 'r') as transactions_f:
            json_data = json.loads(transactions_f)
            for k, transaction in json_data.items():
                print(k, transaction)
        return json_data

    def cash_payment():

        counter = 0
        trials = 3
        while counter < 3:
            cash_payment = input('Enter the amount of cash you want to pay: ')
            counter += 1
            trials -= 1
            if counter == 3:
                print('No', trials, 'trials left. You\'ve been redirected to the main menu.' )
                after_menu2()
            else:
                if trials == 1:
                    print('Only', trials, 'trial left.')
                elif cash_payment.isdigit() != True:
                    print("Not number was entered. Please, try again.")
                    print('Only', trials, 'trials left.')
                elif int(cash_payment) <= 0:
                    print("Got no cash. Please, try again.")
                    print('Only', trials, 'trials left.')
                else:
                    break
        cash_payment = int(cash_payment)
        with open(username + '_balance.data.json', 'r') as balance_f:
            balance_data = json.load(balance_f)
            for k,balance in balance_data.items():
              balance += cash_payment
              balance_data = {'balance:': balance}
              with open(username +'_balance.data.json', 'w') as balance_f:
                  balance_f.write(json.dumps(balance_data))
              print('Your current', k, balance)

        trans_data = {username: cash_payment}
        with open(username + '_transactions.json', 'a', encoding = 'utf-8') as transactions_f:
            json.dump(trans_data, transactions_f, indent=2, ensure_ascii=False)

        return balance_data

    def withdraw_money():

        counter = 0
        with open(username + '_balance.data.json', 'r') as balance_f:
            balance_data = json.load(balance_f)

        while counter < 3:
            input_withdraw = input('Enter the amount of cash you want to withdraw: ')
            counter += 1
            if counter == 3:
                after_menu2()
            else:
                if input_withdraw.isdigit() != True:
                    print("Not number was entered. Please, try again.")
                    counter += 1
                elif int(input_withdraw) > balance_data['balance:']:
                    print("Insufficient funds. Please, try again.")
                    counter += 1
                else:
                    break

        cash_withdraw = int(input_withdraw) * -1
        for k,balance in balance_data.items():
              balance += cash_withdraw
              balance_data = {'balance:': balance}
              with open(username + '_balance.data.json', 'w') as balance_f:
                  balance_f.write(json.dumps(balance_data))
              print('Your current', k, balance)

        trans_data = {username: cash_withdraw}
        with open(username + '_transactions.json', 'a', encoding = 'utf-8') as transactions_f:
            json.dump(trans_data, transactions_f, indent=2, ensure_ascii=False)
        return balance_data

    menu2_switch = {
                    1: cash_payment,
                    2: withdraw_money,
                    3: view_balance,
                    4: view_transaction_history
                    }

    menu2 = operations_menu()
    for key in menu2:
        print(key, '->', menu2[key])
    choice2 = int(input('Enter the number of your choice: '))
    output2 = menu2_switch.get(choice2)()

def incasator_operations():

    incas_oper = {
                 'View banknotes in stock': 1,
                 'Load banknotes': 2,
                 }

    return incas_oper

def incasator_mode():

    def view_banknotes():

        try:
            with open('currency.json', 'r') as currency_f:
                currency_data = json.load(currency_f)
        except:
            currency_data = {}

        for denomination, amount in currency_data.items():
            print('There are in stock:', amount, 'banknotes of denomination', denomination)
        return currency_data

    def load_banknotes():


    try:
        with open('currency.json', 'r') as currency_f:
            currency_data = json.load(currency_f)
    except:
        currency_data = {}
    denomination_amount = int(input('Enter the amount of denominations you want to load: '))
    for i in range(denomination_amount):
        denominat = int(input('Enter the bank note denomination: '))
        amount = int(input('Enter the amount of bank notes: '))
        funds = {denominat: amount}
        funds_i = funds.items()
        currency_data_i = currency_data.items()
        for k,v in currency_data_i:
            for i,j in funds_i:
                if k == i:
                    v = v + amount
            new_funds = {k: v}
            currency_data.update(new_funds)
            with open('currency.json', 'w') as currency_f:
                json.dump(new_funds, currency_f, indent=2, ensure_ascii=False)
                # else:
            #     with open('currency.json', 'a') as currency_f:
            #         json.dump(funds, currency_f, indent=2, ensure_ascii=False)

        return funds

def fin_or_cont():

    fin_or_cont = {
                'Finish': 1,
                'Back to previous menu': 2
                  }
    return fin_or_cont

def after_menu2():

    def finish():

        fin = sys.exit()
        return fin

    def back_to_menu2():

        menu2()
        return menu2()


    after_menu2_switch = {
                  1: finish,
                  2: back_to_menu2,
                  }

    after_menu2 = fin_or_cont()
    for key in after_menu2:
        print(key, '->', after_menu2[key])
    choice3 = int(input('Enter the number of your choice: '))
    output3 = after_menu2_switch.get(choice3)()
    # print(output3)

menu1()
menu2()
after_menu2()
