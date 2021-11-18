# Write a script to sum of the first n positive integers
positive_integers = int(input('Enter the number of integers: '))
x = int(input('Enter the number: '))
total = 0
count = 0
while x >= 1:
    total += x
    count += 1
    x = int(input('Enter the number: '))
    if count == positive_integers:
        break
print (total)
