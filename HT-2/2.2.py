# Написати скрипт, який пройдеться по списку, який складається із кортежів,
# і замінить для кожного кортежа останнє значення.
# Список із кортежів можна захардкодити. Значення, на яке замінюється останній
# елемент кортежа вводиться користувачем.
# Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком).
# Кількість елементів в кортежу повинна бути різна.
lst = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
nmbr = int(input("Enter your number: "))
newlist = []
for i in lst:
    newlist.append(i[0:-1]+(nmbr,))
print(newlist)
