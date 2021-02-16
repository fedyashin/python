list_cubes = []
counter_1 = 1
while counter_1 <= 1000:
    if counter_1 % 2:
        list_cubes.append(counter_1 ** 3)
    counter_1 += 1
sum_all = 0

for counter_2 in range(len(list_cubes)):
    num = list_cubes[counter_2]
    sum_digits = 0
    while num > 0:
        remains = num % 10
        sum_digits += remains
        num //= 10
    if sum_digits % 7 == 0:
        print("Число:", list_cubes[counter_2], "сумма цифр:", sum_digits)
        sum_all += list_cubes[counter_2]
print("Сумма чисел из списка:", sum_all)

for counter_3 in range(len(list_cubes)):
    list_cubes[counter_3] += 17

sum_all_17 = 0
for counter_4 in range(len(list_cubes)):
    num = list_cubes[counter_4]
    sum_digits = 0
    while num > 0:
        remains = num % 10
        sum_digits += remains
        num //= 10
    if sum_digits % 7 == 0:
        print("Число:", list_cubes[counter_4], "сумма цифр:", sum_digits)
        sum_all_17 += list_cubes[counter_4]
print("Сумма чисел из списка:", sum_all_17)
