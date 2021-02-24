from requests import get, utils


def currency_content(list_code, position_code=0):  # Функция парсер кодов валют
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    while True:
        position_code = content.find('<CharCode>', position_code)
        if position_code < 0:
            break
        list_code.append(content[position_code + 10: position_code + 13])
        position_code += 13


def currency_rates(list_code, currency):   # Функция парсер курса валют
    for inx in list_code:
        if inx == currency:
            response = get('http://www.cbr.ru/scripts/XML_daily.asp')
            encodings = utils.get_encoding_from_headers(response.headers)
            content = response.content.decode(encoding=encodings)
            position_currency = content.find(currency)
            position_exchange = content.find('<Value>', position_currency) + 7
            print(f'На {content[60:70]} курс 1 {currency} = {content[position_exchange:position_exchange + 5]} руб.')
