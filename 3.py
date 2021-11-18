# Write a script to concatenate N strings
positive_integers = int(input('Enter the number of integers: '))
total = 0
count = 0
while positive_integers >= 1:
    x = int(input('Enter the number: '))
    total += x
    count += 1
    if count == positive_integers:
        break
print (total)
