# 3.Написати функцию < is_prime >, яка прийматиме 1 аргумент -
# число від 0 до 1000, и яка вертатиме True, якщо це число просте,
# и False - якщо ні

def is_prime(number):
    for i in range(2, number // 2+1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        print("True")
    else:
        print("False")

k = 0
number = int(input('Enter the number: '))

is_prime(number)
