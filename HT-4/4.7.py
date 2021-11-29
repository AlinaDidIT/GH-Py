# 7. Написати функцію, яка приймає на вхід список і підраховує
# кількість однакових елементів у ньому.

def doubles(lst):

    doubles_dict = {i:lst.count(i) for i in lst if lst.count(i) > 1}
    return doubles_dict

some_list = [1,"a", 1, "b", 5, "a", "c", 3, "c", "a", 5, "c"]
print(doubles(some_list))
