# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

from sys import argv
from requests import get, utils


def currency_content(position_code=0):  # Функция парсер кодов валют
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    while True:
        position_code = content.find('<CharCode>', position_code)
        if position_code < 0:
            break
        list_code.append(content[position_code + 10: position_code + 13])
        position_code += 13


def currency_rates(currency):   # Функция парсер курса валют
    for inx in list_code:
        if inx == currency:
            response = get('http://www.cbr.ru/scripts/XML_daily.asp')
            encodings = utils.get_encoding_from_headers(response.headers)
            content = response.content.decode(encoding=encodings)
            position_currency = content.find(currency)
            position_exchange = content.find('<Value>', position_currency) + 7
            print(f'На {content[60:70]} курс 1 {currency} = {content[position_exchange:position_exchange + 5]} руб.')


list_code = []
currency_content()
currency_rates(argv[1].upper())

# Результат:
# C:\Users\Fedyashin\PycharmProjects\Fedyashin_Vyacheslav_dz_4>venv\Scripts\python task_4_5.py usd
# На 25.02.2021 курс 1 USD = 73,75 руб.
#
# C:\Users\Fedyashin\PycharmProjects\Fedyashin_Vyacheslav_dz_4>venv\Scripts\python task_4_5.py eur
# На 25.02.2021 курс 1 EUR = 89,66 руб.
