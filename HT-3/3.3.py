# 3. Написати функцiю season, яка приймає один аргумент —
# номер мiсяця (вiд 1 до 12), яка буде повертати пору року,
# якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season(month):
    seasons = {'Winter': (1, 2, 12),
               'Spring': (3, 4, 5),
               'Summer': (6, 7, 8),
               'Autumn': (9, 10, 11)}
    for season, months in seasons.items():
        if month in months:
            print(season)
            
month = int(input('Enter the number of a month: '))
season(month)
