import time


class Date:
    def __init__(self, line: str):
         self.validate_numbers(Date.get_numeric(line))

    @classmethod
    def get_numeric(cls, line_date: str):
        return list(map(int, line_date.split("-")))

    @staticmethod
    def validate_numbers(numbers: list):
        # d, m, y = numbers
        """ от чего уходил к тому и возвращаю"""
        my_date = "-".join(str(x) for x in numbers)
        try:
            valid_date = time.strptime(my_date, '%d-%m-%Y')
        except ValueError:
            print("Не верная дата!")
        else:
            print("Дата верная")
        """Проверку по месяцам не делал"""
        # assert 1 <= d <= 31, "Неверный формат числа"
        # assert 1 <= m <= 12, "Неверный формат месяца"
        # assert 1970 <= y <= 2100, "Неверный формат года"


test_1 = Date("11-1-2021")
test_2 = Date("41-1-2021") #error
