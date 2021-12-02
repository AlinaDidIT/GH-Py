# 3. На основі попередньої функції створити наступний кусок кода:
  #  а) створити список із парами ім'я/пароль різноманітних видів
  #  (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
  #  б) створити цикл, який пройдеться по цьому циклу і, користуючись
  #  валідатором, перевірить ці дані і надрукує для кожної пари значень
  #  відповідне повідомлення, наприклад:

class LoginException(Exception):
    pass

def login(users):
    status = ''
    try:
        for user in users:
                if len(user[0])>3 and len(user[0])<50 and len(user[1]) > 8:
                    for s in user[0]:
                        if s[0].isupper() == True:
                            if any(s.isdigit() for s in user[1]) == True:
                                status = 'Ok'
                                print('Username:', user[0], '\nPassword:', user[1], '\nStatus:', status)
                                
    except LoginException:
        print('False')

users = [['Chucha', 'dfjkghlskdjhg'], ['df', '45687532'], ['Dima', 'sdfgs54sdfg'], ['sunRise', 'sdjkjhjh98']]
login(users)
