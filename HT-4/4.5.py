# 5. Написати функцію < fibonacci >, яка приймає один аргумент
# і виводить всі числа Фібоначчі, що не перевищують його.

def fibonacci(i):
    a, b = 1, 1
    for i in range(i):
        yield a
        a, b = b, a + b
    return

i = int(input('Enter the number: '))
print(list(fibonacci(i)))
