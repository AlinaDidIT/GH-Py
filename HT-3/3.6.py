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
import re
def nocontext():
    some_text = input('Enter some string: ')
    len_text = len(some_text)
    if 30 <= len_text <= 50:
        print(len_text)
    elif len_text < 30:
        num_list = re.findall('\d+', some_text)
        nums = [int(item) for item in num_list]
        total = sum(nums)
        print(total)
        only_text = re.sub(r"\d+",'',some_text)
        print(only_text)
    elif len_text > 50:
        print (some_text[:len_text//2])
        print (some_text[len_text//2:])
nocontext()
