def func_div(a, b):
    """Возвращает частное от деления.

    """
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return "Division by zero"


def get_number(word: str = "первое"):
    """Запрашивает число и пытается ковентировать в 'float'.

    Именованные параметры:
    word -- слово для запроса (по умолчанию "первое")

    """

    try:
        first = float(input(f"Введите {word} число: "))
    except ValueError:
        return False
    else:
        return first


x = get_number()
y = get_number("второе")

if x and y:
    print(func_div(x, y))
else:
    print("Один из аргументов не является числом")
