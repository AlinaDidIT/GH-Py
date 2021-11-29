# 8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів
# в списку. Тобто, функція приймає два аргументи: список і величину зсуву
# (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна -
# навпаки - пересуваємо елементи з початку списку в його кінець).

import collections

def move_items(lst, move):
    lst = collections.deque(lst)
    lst.rotate(move)
    move = list(lst)
    return  move

lst = [1, 2, 3, 4, 5]


move = int(input("Enter shift value: "))
print(lst, 'shift=', move, ' -->', move_items(lst, move))
