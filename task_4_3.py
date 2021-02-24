# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.

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
print('Курс валюты онлайн, по данным с сайта Банка России.')
print(list_code)
while True:
    currency_code = input('Введите код валюты (USD, EUR, ...), или нажмите Enter для выхода')
    if currency_code == "":
        break
    elif currency_code.isalpha():
        currency_rates(currency_code.upper())
