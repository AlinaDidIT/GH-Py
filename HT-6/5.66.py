#6. Всі ви знаєте таку функцію як <range>.
# Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції -
# можна почитати документацію по ній:
# https://docs.python.org/3/library/stdtypes.html#range

def gen(user_input):
    for i in range(1, iter_obj+1, 5):
            yield i/100*20


user_input = int(input('Enter your number: '))
for i in gen(user_input):
    print(i)
