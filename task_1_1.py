duration = 1
while duration > 0:
    duration = int(input("Введите кол-во секунд (или 0 для остановки)"))
    if duration <= 59:
        print(duration, "сек")
    elif duration <= 3599:
        print(duration // 60, "мин", duration % 60, "сек")
    elif duration <= 86399:
        print(duration // 3600, "час", duration % 3600 // 60, "мин", duration % 60, "сек")
    elif duration >= 86400:
        print(duration // 86400, "дн", duration % 86400 // 3600, "час",
              duration % 3600 // 60, "мин", duration % 60, "сек")
