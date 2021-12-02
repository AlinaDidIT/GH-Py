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
    pass

def login(username, password, silent = False):
    users = [['Andrew', 'F984jvPHj9'], ['Eugen', 'F956jvPHj9'], ['Hanna', 'G5jm5D9p9P'], ['Olha', '8f7b8U7VrR'], ['Dmytro', 'u7L4Y85tJu']]
    user = [username, password]
    if silent == False:
        if any(default_user == user for default_user in users) == True:
            print(True)
        else:        
            raise LoginException("Not valid input")
    else:        
        print(False)     
username = input('Enter the username: ')
password = input('Enter the password: ')

login(username, password)
