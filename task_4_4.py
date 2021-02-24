# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.
import task_4_4_utils

list_code = []
task_4_4_utils.currency_content(list_code)
print('Курс валюты онлайн, по данным с сайта Банка России.')
print(list_code)
while True:
    currency_code = input('Введите код валюты (USD, EUR, ...), или нажмите Enter для выхода')
    if currency_code == "":
        break
    elif currency_code.isalpha():
        task_4_4_utils.currency_rates(list_code, currency_code.upper())
