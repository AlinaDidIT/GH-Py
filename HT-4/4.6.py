# 6. Вводиться число. Якщо це число додатне, знайти його квадрат,
# якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.

def operations(number):
    if number < 0:
        result = number + 100
    elif number > 0:
        result = number ** 2
    else:
        result = 0
    return result

number = int(input("Enter your number: "))

print(operations(number))
