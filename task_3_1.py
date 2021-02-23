# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте: как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
# в теле функции или снаружи?

def num_translate(num):
    if dict_translate.get(num) is not None:
        print(dict_translate[num])


print('Переводчик чисел.')
dict_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
while True:
    number = input('Введите прописью число от 0 до 10 на английском языке для перевода, или нажмите Enter для выхода')
    if number == "":
        break
    num_translate(number.lower())
