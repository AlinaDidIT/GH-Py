# 3. На основі попередньої функції створити наступний кусок кода:
  #  а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
  #  б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення

  
# Вибачте, вона працює неправильно, поки що я дуже туплю в цій темі:(((((((((

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
            raise LoginException("The password must include at least one digit")    
        else:
            print('Ok')

users = [['Chucha', 'dfjkghlskdjhg'], ['df', '45687532'], ['Dima', 'sdfgs54sdfg'], ['sunRise', 'sdjkjhjh98']]
for user in users:
    print('Name:', user[0], '\nPassword:', user[1], '\nStatus:', login(user[0], user[1]))
