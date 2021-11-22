# Написати скрипт, який залишить в словнику тільки пари із
# унікальними значеннями (дублікати значень - видалити).
# Словник для роботи захардкодити свій.

people = {'Andrew': 39, 'Ben': 25, 'Rick': 48, 'David': 39}
values = set()
new_people = {}

for k, v in people.items():
    if v not in values:
        new_people.update({k: v})
        values.add(v)
print(new_people)
