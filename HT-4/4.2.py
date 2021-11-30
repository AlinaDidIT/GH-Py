# 2. Написати функцію < bank > , яка працює за наступною логікою: користувач
# робить вклад у розмірі < a > одиниць строком на < years > років під
# < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також
# нараховуються відсотки). Параметр < percents > є необов'язковим і має
# значення по замовчуванню < 10 > (10%). Функція повинна принтануть і
# вернуть суму, яка буде на рахунку.

def bank(a, years, percents = 10):
    balance = a
    for i in range(2, years+1):
        a = a
        balance += balance/100*percents
        print(round(balance,2))

a = int(input('Enter the amount of your bank deposit: '))
years = int(input('Enter the amount of years of your deposit: '))
bank(a, years)
