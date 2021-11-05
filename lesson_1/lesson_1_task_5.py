income = int(input("Введите выручку: "))
decline = int(input("Введите издержки: "))

if income > decline:
    print("Фирма работатет в прибыль")
    print("Рентабельность выручки {0:.0%}".format((income / decline) - 1))
    personals = int(input("Введите количество сотрудников: "))
    print("Прибыль фирмы в расчете на одного сотрудника: {0:.2f}".format((income - decline) / personals))
elif income < decline:
    print("Фирма работатет в минус, она не рентабильна")
else:
    print("Фирма работатет в '0'")
