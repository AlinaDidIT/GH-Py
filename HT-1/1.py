# Write a script which accepts a sequence
# of comma-separated numbers from user and
# generate a list and a tuple with those numbers
numbers = input('Enter your numbers here: ')
lst = numbers.split(",")
tpl = tuple(lst)
print(lst)
print(tpl)
