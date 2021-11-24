# 4. Створiть 3 рiзних функцiї (на ваш вибiр).
# Кожна з цих функцiй повинна повертати якийсь результат.
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
# обробляє повернутий ними результат та також повертає результат.
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def total():
    x = int(input('Enter your number: '))
    total = 0
    for i in range(x+1):
        total += i
    return total

def ranging():
  x = input('Enter your range: ').split('-')
  x = [int(item) for item in x]
  return x

def ranging():
    x = 
