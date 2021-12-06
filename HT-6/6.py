# 1. Програма-світлофор.
# Створити програму-емулятор світлофора для авто і пішоходів.
# Після запуска програми на екран виводиться в лівій половині -
# колір автомобільного, а в правій - пішохідного світлофора.
# Кожну секунду виводиться поточні кольори. Через декілька ітерацій -
# відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.


import time

def streetlight():
    colors = ['Red', 'Yellow', 'Green', 'Yellow']
    while True:
        traffic = colors[2]
        for i in colors:
            times = 4
            if i == colors[2]:
                traffic = colors[0]
            elif i == 'Yellow':
                times = 2
            for t in range(times):
                time.sleep(1)
                print('\t',i,'\t',traffic)
streetlight()
