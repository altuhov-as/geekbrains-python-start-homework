def my_func(val_1, val_2):
    return val_1**val_2


def my_func_2(k, l):
    result = 1
    while l != 0:
        result /= k
        l += 1
    return result


def is_int(test):
    """Фунция проверяет можно ли текст конвентировать в цисло"""
    try:
        int(test)
        return True
    except ValueError:
        return False


x, y = "", ""
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    else:
        x, y = (input("Введите число a: ")), (input("Введите степень b: "))
        if (is_int(x) and int(x) > 0) and (is_int(y) and 0 > int(y)):
            print("Результат вычислений:", my_func(int(x), int(y)))
            print("Вторая вариант:", my_func_2(int(x), int(y)))
        else:
            print("Ошибка входных данных.\n"
                  "'X' -действительное положительное число\n"
                  "'Y' - целое отрицательное число")
