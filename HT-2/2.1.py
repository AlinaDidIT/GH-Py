# Написати скрипт, який конкатенує всі елементи в списку
# і виведе їх на екран. Список можна "захардкодити".
# Елементами списку повинні бути як рядки, так і числа.
lst = ['hello', '34', 'common', '658', 'project', 'task', '38']
lst = sorted(lst)
num_lst1 = 0
str_lst2 = 0
lst1 = list(lst[0:3])
for i in lst1:
    num_lst1 += int(i)
lst2 = list(lst[3:])
for b in lst2:
    str_lst2 = ''.join(lst2)
print(num_lst1, str_lst2)
