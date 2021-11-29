# 5. Написати функцію < fibonacci >, яка приймає один аргумент
# і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(i):
    a = 0
    b = 1
    fibo_list=[a, b]
    while b < i:
        a, b=b, a+b
        fibo_list.append(b)
    fibo_list.pop(-1)
    print(fibo_list)

i = int(input('Enter the number: '))
fibonacci(i)
