number = int(input("введите число от 0 до 20: "))

if number ==0:
    print(number, "процентов")
elif number == 1:
    print(number, "процент")
elif number >= 2 and number <= 4:
    print(number, "процента")
elif number >= 5 and number <= 20:
    print(number, "процентов")
else:
    print("вы ввели не-верное число")
print("0 процентов, 1 процент, 2 - 4 процента, 5-20 процентов")