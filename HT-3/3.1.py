# 1. Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне значення,
# якщо остача від ділення на 17 дорівнює 0.

cycle = int(input('Enter your number: '))
for i in range(1, cycle+1):
    if i%17 == 0:
        print(i)
