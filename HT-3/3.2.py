# Користувачем вводиться початковий і кінцевий рік. Створити цикл,
# який виведе всі високосні роки в цьому проміжку (границі включно).
years = input('Enter the interval using \'-\': ').split('-')
years = [int(item) for item in years]
for i in range(years[0], years[1]+1):
    if i%400 == 0 or i%4 == 0 and i%100 != 0:
        print(i)
