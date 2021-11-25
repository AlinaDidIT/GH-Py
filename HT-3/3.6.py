# 6. Маємо рядок --> 
#"f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3k
#j546p465jnpoj35po6j345" -> просто потицяв по клавi
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього,
# яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину,
# кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо
# рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя
def nocontext():
    some_text = input('Enter some string: ')
    numbers = 0
    letters = 0
    for symbol in some_text:
        if symbol.isdigit():
            numsum += int(symbol)
            numbers += 1
    for symbol in some_text:
        if symbol.isalpha():
            allletters += symbol
            letters += 1
    if 30 <= len_text <= 50:
        print('Length: ', len(some_text))
        print('Numbers: ', len(numbers))
        print('Letters: ', len(letters))
    elif len_text < 30:
        print('The sum of numbers: ', numsum)
        print('String without numbers: ','.join(allletters)')
    elif len_text > 50:
        print (some_text[:len_text//2])
        print (some_text[len_text//2:])
nocontext()
