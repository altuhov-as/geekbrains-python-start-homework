def int_func(text: str = "simple"):
    """Принимает слово, возвращает слово с заглавной буквы.

    Именованные параметры:
    text -- строка (по умолчанию "simple")

    """
    return text.title()


def int_func_2(text: str = "simple", alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    """Принимает предложение, возвращает список слов (латиницей) с заглавной буквы."""
    tmp_list = text.split()
    result = []
    for tmp in tmp_list:
        """ЗаЯндексил 'intersection'"""
        if tmp.isalpha() and not alphabet.intersection(set(tmp.lower())):
            """я бы предпочел использовать '.capitalize()' """
            result.append(int_func(tmp))
    return result


print(int_func())
print(" ".join(int_func_2("nice 5good авп ъghj jапро hjjпаро вапрghgh cool")))
