# Написати функцію < square > , яка прийматиме один аргумент -
# сторону квадрата, і вертатиме 3 значення (кортеж): периметр
# квадрата, площа квадрата та його діагональ

def square(side):
    p = side*4
    s = side*side
    d = ((2*side**2)**0.5)
    d = round(d,2)
    calculations = (p,s,d)
    print(calculations)

side = float(input('Enter the lenght of a side of the square: '))
square(side)
