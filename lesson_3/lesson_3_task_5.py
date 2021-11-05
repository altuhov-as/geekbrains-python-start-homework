all_sum = 0
exit_symbol = "Q"
do_exit = False
while not do_exit:
    """
    Хотел использовать такой ввод данных, но лишние действия по преобразованию
    a, b, *c = input("Enter: ").split() 
    """
    numbers = input("Введите строку из чисел через пробел: ").split()
    for number in numbers:
        if number.isdigit():
            all_sum += int(number)
        elif number.upper() == exit_symbol:
            do_exit = True
            break
        else:
            print("Данные не корректын, повторите ввод данных")
    print("Общая сумма =", all_sum)
