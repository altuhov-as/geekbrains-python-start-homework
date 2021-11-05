class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str = "Ivan", surname: str = "Ivanov", position: str = "FreeDom",
                 wage: int = 0, bonus: int = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}."

    def get_total_income(self):
        return f"Доход в месяц = {sum(self._income.values())}"


maksim = Position("Максим", "Петров", "Курьер", 1000, 50)
print(maksim.get_full_name(), maksim.get_total_income())
