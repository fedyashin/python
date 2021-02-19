# Создать список, содержащий цены на товары (10 – 20 товаров), например:
# [57.8, 46.51, 97, ...]
# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если,
# например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# - Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# - Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
import random

product_prices_lst = []
inx = 1
while inx <= (random.randint(10, 20)):
    product_prices_lst.append(random.randrange(100, 10000) / 100)
    inx += 1

id_before_sort = id(product_prices_lst)
product_prices_lst.sort()
id_after_sort = id(product_prices_lst)
if id_before_sort == id_before_sort:
    print(f'Объект списка после сортировки остался тот же: {id_before_sort} = {id_after_sort}')

product_prices_text = []
str_product_prices = str()
for elem in product_prices_lst:
    elem = str(elem).split('.')
    product_prices_text.append(f"{elem[0]} руб {elem[1]} коп")
str_product_prices = ', '.join(product_prices_text)
print(str_product_prices)

product_prices_lst_2 = sorted(product_prices_lst.copy(), reverse=True)

product_prices_text_2 = []
str_product_prices_max = str()
counter = 0
for elem in product_prices_lst_2:
    if counter < 5:
        elem = str(elem).split('.')
        product_prices_text_2.append(f"{elem[0]} руб {elem[1]} коп")
        counter += 1
    else:
        break
str_product_prices_max = ', '.join(product_prices_text_2)
print(str_product_prices_max)
