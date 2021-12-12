import json
import pprint

class LoginException(Exception):
    pass

class NumberException(Exception):
    pass

def login_menu():
    login_menu = {
                'Authotization': 1,
                'Registration': 2,
                }
    return login_menu

def menu1():

    def validator(username, password):

          if len(username)<3 or len(username)>25:
              raise LoginException("The username must be more than 3 and less than 25 symbols")
          elif username[0].isupper() != True:
              raise LoginException("The first letter of the username must be upper case")
          elif len(str(password)) != 4:
              raise LoginException("The password must consist of 4 numbers")
          elif type(password) != int:
              raise LoginException("The password must include only digits")
          else:
              return '\n\nValidation is successful'

    def balance_file(username):

        balance = {'balance:': 0}
        with open(username + '_balance.data.json', 'w') as balance_f:
            json.dump(balance, balance_f, indent=2, ensure_ascii=False)
        return balance

    def transactions_file(username):

        transaction = {username: 0}
        with open(username + '_transactions.json', 'w') as transactions_f:
            json.dump(transaction, transactions_f, indent=2, ensure_ascii=False)
        return transaction

    def registration(username, password):

        try:
            with open('users.data.json') as file:
                users_data = json.load(file)
        except:
            users_data = {}

        user = {username: password}
        user_i = user.items()
        users_data_i = users_data.items()
        for k,v in user_i:
            if user_i & users_data_i == user_i:
                print('\n\nYour account already exists.')
            else:
                users_data.update(user)
                validator(username, password)
                with open('users.data.json', 'w') as file:
                    json.dump(users_data, file, indent=2, ensure_ascii=False)
                print('\n\nCongratulations! You\'ve got your personal card :)')
        return users_data

    def authorization(username, password):

        print('\n\nHello!')
        user = {username: password}
        with open('users.data.json') as file:
            users_data = json.load(file)
            user_i = user.items()
            users_data_i = users_data.items()
            for k,v in user_i:
                if user_i & users_data_i == user_i:
                    print('\n\nPlease, choose the operation: ')
                else:
                    print('Sorry, there is no such client.\n\nTo SignUp, please, enter 'r' button or try again: ')
                    # показать меню авторизации
        return user

    menu1_switch = {
                    1: authorization,
                    2: registration
                    }

    menu1 = login_menu()
    print('Welcome! Choose the SignUP or LogIn operation.\n\n(To continue press any other button) : ')
    for key in menu1:
        print(key, '->', menu1[key])
    choice1 = int(input('Enter the number of your choice: '))
    output1 = menu1_switch.get(choice1)()
    if choice1 == 2:
        choice = 1
        output1 = menu1_switch.get(choice1)()
    else:
        pass

def operations_menu():

    operations_menu = {
                'Cash payment': 1,
                'Withdraw money': 2,
                'View balance': 3,
                'View transaction history': 2,
                }
    return operations_menu

def menu2():

    def view_balance():

        with open(username +'_balance.data.json', 'r') as balance_f:
            balance_data = json.load(balance_f)
            for k,balance in balance_data.items():
                print('Your current', k, balance)

    def view_transaction_history(transactions_file_json):

        with open(username +'_transactions.data.json', 'r') as transactions_f:
            json_data = json.loads(transactions_f)
            for k, transaction in json_data.items():
                print(k, transaction)
        return json_data

    def cash_payment(username):

        cash_payment = int(input('Enter the amount of cash you want to pay: '))
        if type(cash_payment) == int:
            with open(username +'_balance.data.json', 'r') as balance_f:
                balance_data = json.load(balance_f)
                for k,balance in balance_data.items():
                  balance += cash_payment
                  balance_data = {'balance:': balance}
                  with open(username +'_balance.data.json', 'w') as balance_f:
                      balance_f.write(json.dumps(balance_data))
                  print('Your current', k, balance)

            trans_data = {username: cash_payment}
            with open(username +'_transactions.json', 'a', encoding = 'utf-8') as transactions_f:
                json.dump(trans_data, transactions_f, indent=2, ensure_ascii=False)
        else:
            raise NumberException("Not number was entered. Please, try again.")
        return balance_data

    def withdraw_money(username):

        input_withdraw = int(input('Enter the amount of cash you want to withdraw: '))
        with open(username +'_balance.data.json', 'r') as balance_f:
            balance_data = json.load(balance_f)
        if type(input_withdraw) != int:
            raise NumberException("Not number was entered. Please, try again.")
        elif input_withdraw > balance_data['balance:']:
            raise NumberException("There are not enough funds in the account.")
        else:
            cash_withdraw = -input_withdraw
            for k,balance in balance_data.items():
              balance += cash_withdraw
              balance_data = {'balance:': balance}
              with open(username +'_balance.data.json', 'w') as balance_f:
                  balance_f.write(json.dumps(balance_data))
              print('Your current', k, balance)

            trans_data = {username: cash_withdraw}
            with open(username +'_transactions.json', 'a', encoding = 'utf-8') as transactions_f:
                json.dump(trans_data, transactions_f, indent=2, ensure_ascii=False)

        return balance_data

    menu2_switch = {
                    1: view_balance,
                    2: view_transaction_history,
                    1: cash_payment,
                    2: withdraw_money
                    }

    menu2 = operations_menu()
    for key in menu2:
        print(key, '->', menu2[key])
    choice2 = int(input('Enter the number of your choice: '))
    output2 = menu2_switch.get(choice2)()


    # def withdraw_money():
    # # видача грошей для користувачів відбувається в межах наявних купюр;
    # # Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом -
    # # видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням
    # # "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) -
    # # в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн.,
    # # а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує
    # # видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
    #
    # def cash():
    # # перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
    #
    # def pay_cash():
    #     # якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат -
    #     # не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все,
    #     # що в нього входить, відкладає в окрему касету.
    #
    # # у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
    # #      - переглянути наявні купюри;
    # #      - змінити кількість купюр;
    # # режим як "інкассація", за допомогою якого в нього можна
    # # "загрузити" деяку кількість банкнот (вибирається номінал і кількість)

menu1()
menu2()

username = input('Please, enter your username: ')
password = int(input('Enter your password (4 digits): '))
