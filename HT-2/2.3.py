# Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".

lst = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', ['',]]
lst[:] = [item for item in lst if item and item != ('',) and item != ['',]]
print(lst)
