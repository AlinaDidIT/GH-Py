# Write a script to convert decimal to hexadecimal
decimal = int(input('Enter the number: '))
hexadecimal = hex(decimal)
noprefix_hex = hexadecimal.replace('0x', '')
print(noprefix_hex)
