# Write a script to concatenate N strings
number_of_strings = int(input('Enter the number of strings: '))
count = 0
newstring = ""
while number_of_strings:
    x = input('Enter a string: ')
    newstring += x
    count += 1
    if count == number_of_strings:
        break
print (newstring)
