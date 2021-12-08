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
#       - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні -
#       вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#       - потім - елементарне меню типа:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив :)

class LoginException(Exception):
    pass

def take_card(card):
    if card == 'c':
        return 'Hello!'

def login(username, password):

        if len(username)<3 or len(username)>25:
            raise LoginException("The username must be more than 3 and less than 25 symbols")
        elif username[0].isupper() != True:
            raise LoginException("The first letter of the username must be upper case")
        elif len(password) != 3:
            raise LoginException("The password must consist of 4 digits")
        elif all(s.isdigit() for s in password) != True:
            raise LoginException("The password must include only digits")
        else:
            print('Ok')

insert_card = input('Please insert your card. (Press "c")')
take_card(insert_card)

user = input('PLease, enter your USERNAME and PASSWORD with the "space" separator').split(' ')
with open('hello.txt', 'r', encoding='utf-8') as file:
    users = file.readlines()
    try:
        for i in users:
            if user == i:
                login(user[0], user[1])
    except LoginException as err:
        print(err)
