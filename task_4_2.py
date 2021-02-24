# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую курс
# этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

from requests import get, utils


def currency_rates(currency):
    for inx in tuple_code:
        if inx == currency:
            response = get('http://www.cbr.ru/scripts/XML_daily.asp')
            encodings = utils.get_encoding_from_headers(response.headers)
            content = response.content.decode(encoding=encodings)
            position_currency = content.find(currency)
            position_exchange = content.find('<Value>', position_currency) + 7
            res_chang = float(content[position_exchange:position_exchange + 5].replace(",", "."))
            return res_chang


tuple_code = 'USD', 'EUR'
print('Курс валюты онлайн, по данным с сайта Банка России.')
while True:
    currency_code = input('Введите код валюты (USD, EUR), или нажмите Enter для выхода')
    if currency_code == "":
        break
    elif currency_code.isalpha():
        result_change = currency_rates(currency_code.upper())
        if result_change is not None:
            print(f' 1 {currency_code.upper()} = {result_change} руб.')
