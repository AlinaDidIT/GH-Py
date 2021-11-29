# 4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - 
# початок і кінець діапазона, і вертатиме список простих чисел
# всередині цього діапазона.

def prime_list(start, finish):
    lst = []
    for i in range(start, finish+1):
        k = 0
        for j in range(1,i+1):
            if i%j == 0:
                k += 1
        if k == 2:
            lst.append(i)
    print(lst)

start = int(input('Enter the begining of your range: '))
finish = int(input('Enter the ending of your range: '))

prime_list(start, finish)
