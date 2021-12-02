# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   #- ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   #- пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   #- щось своє :)
   #Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом

class LoginException(Exception):
    pass

def login(username, password):

    if len(username)<3 or len(username)>50:
        raise LoginException("The username must be more than 3 symbols and less than 50")
    elif username[0].isupper() != True:
        raise LoginException("The first letter of the username must be upper case")
    elif len(password) < 8:
        raise LoginException("The password must be more than 8 symbols")
    elif any(s.isdigit() for s in password) != True:
        raise LoginException("The password must include at list one digit")
    else:
        print('Your login parameters are correct')

username = input('Enter the username: ')
password = input('Enter the password: ')

login(username, password)
