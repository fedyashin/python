list_percent = ['процент', 'процента', 'процентов']
num = 0
while num < 100:
    num = int(input("Введите число от 1 до 20 (или 100 для остановки)"))
    if num == 1:
        print(num, list_percent[0])
    elif 2 <= num <= 4:
        print(num, list_percent[1])
    elif 5 <= num < 100:
        print(num, list_percent[2])
    elif num > 99:
        break
