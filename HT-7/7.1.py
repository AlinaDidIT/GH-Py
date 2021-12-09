# 1. Програма-банкомат.
#    Створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#       - потім - елементарне меню типа:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив :)
import json

class LoginException(Exception):
    pass

def insert_card(card):
    try:
        if card == 'c':
            return 'Hello!'
    except:
         raise LoginException("Sorry, something went wrong")

def (username, password):

        if len(username)<3 or len(username)>25:
            raise LoginException("The username must be more than 3 and less than 25 symbols")
        elif username[0].isupper() != True:
            raise LoginException("The first letter of the username must be upper case")
        elif len(str(password)) != 4:
            raise LoginException("The password must consist of 4 numbers")
        elif type(password) != int:
            raise LoginException("The password must include only digits")
        else:
            return 'Validation is successful'

user_card = input('Please, insert your card. Enter "c": ')
insert_card(user_card)

username = input('Please, enter your username that starts with uppercase: ')
password = int(input('\n\nThank you!\n\nEnter your password with 4 digits: '))
user = {username:password}

with open("users.data.json", "r") as json_file:
    users = json.load(json_file)
user_i = user.items()
users_i = users.items()
try:
    for k,v in user.items():
        if user_i & users_i == user_i:
            print(login(k,v))
except LoginException as err:
        print(err)
