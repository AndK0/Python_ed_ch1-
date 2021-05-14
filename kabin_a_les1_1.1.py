time = int(input("введите количество секунд: "))

month = time // 2592000 % 12
days = time // 86400 % 30
hours = time // 3600 % 24
minutes = time // 60 % 60
seconds = time % 60

print(f'{month} месяцев {days} дней {hours} час {minutes} мин {seconds} cек')
