# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових
# (<username> та <password>) і третій - необов'язковий параметр <silent>
# (значення за замовчуванням - <False>).
# Логіка наступна:
      # якщо введено коректну пару ім'я/пароль - вертається <True>;
      # якщо введено неправильну пару ім'я/пароль і <silent> == <True> -
      # функція вертає <False>, інакше (<silent> == <False>) -
      # породжується виключення LoginException

class LoginException(Exception):
    def __init__(self, users):
        self.users = users

def login(username, password, silent = False):
    users = dict(zip(username, password))
    for user, password in users.items():
        try:
            if item in users.items() and silent == False:
                print('True')
        except LoginException:
            silent = True
            print('False')

username = ['Andrew', 'Eugen', 'Hanna', 'Olha', 'Dmytro']
password = ['F984jvPHj9', 'G5jm5D9p9P', '8f7b8U7VrR', '93nE9GLc4e', 'u7L4Y85tJu']
users = dict(zip(username, password))
i_am_user = input('Enter your name and parol: ').split(' ')
silent = input('Enter True or False for silent: ')
