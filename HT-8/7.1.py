import json

counter = 0
while counter < 3:      
    username = input('Please, enter your username: ').rstrip()
    password = input('Enter your password (4 digits): ')
    counter += 1
    if counter == 3:
        break
    else:
        if len(username)<3 or len(username)>25:
            print('The username must be more than 3 and less than 25 symbols')
            counter += 1
        elif username[0].isupper() != True:
            print('The first letter of the username must be upper case')
            counter += 1
        elif len(password) != 4:
            print('The password must consist of 4 numbers')
            counter += 1
        elif password.isdigit() != True:
            print('The password must include only digits')
            counter += 1 
        else:
            break
            
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
                print('Sorry, there is no such client.To SignUp, please, enter 'r' button or try again: ')

        return user

    menu1_switch = {
                    1: authorization,
                    2: registration
                    }

    menu1 = login_menu()
    print('Welcome! Choose the SignUP or LogIn operation.(To continue press any other button) : ')
    for key in menu1:
        print(key, '->', menu1[key])
    choice1 = int(input('Enter the number of your choice: '))
    output1 = menu1_switch.get(choice1)()

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

        with open(username +'_balance.data.json', 'r') as balance_f:
            balance_data = json.load(balance_f)
            for k,balance in balance_data.items():
                print('Your current', k, balance)

    def view_transaction_history():

        with open(username +'_transactions.json', 'r') as transactions_f:
            json_data = json.loads(transactions_f)
            for k, transaction in json_data.items():
                print(k, transaction)
        return json_data

    def cash_payment():

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

    def withdraw_money():

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

def currency():

    currency = {
                 1000: 1000, 
                 500: 1000,
                 200: 1000,
                 100: 1000,
                 50: 1000,
                 20: 1000,
                 10: 1000
                 }
    currency = json.dumps(currency, indent=2)
    currency_in_stock = json.loads(currency)
    return currency, currency_in_stock

