# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при
# нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z

x = float(input('Enter the x value: '))
y = float(input('Enter the y value: '))
def cond():
    if x != y:
        if x > y:
            print('X is', x-y, 'greater than Y')
        elif x < y:
            print('Y is', y-x, 'greater than X')
    else:
        print('X equals Y')

cond()
