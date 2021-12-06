#6. Всі ви знаєте таку функцію як <range>.
# Напишіть свою реалізацію цієї функції.
# P.S. Повинен вертатись генератор.
# P.P.S. Для повного розуміння цієї функції -
# можна почитати документацію по ній:
# https://docs.python.org/3/library/stdtypes.html#range

def generator(start, stop=None, step=1):
    if step == 0:
        step = 1
    elif stop != None:
        start,stop = stop,start
    else:
        stop = 0
    try:
        if step > 0:
            while stop < start:
                yield stop
                stop += start
        if step < 0:
            while stop > start:
                yield stop
                stop += step
    except ValueError:
        pass

for i in generator(10, 1, -2):
    print(i)
