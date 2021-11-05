from abc import abstractmethod


class Warehouse:
    technique = {}
    technique_econom = {}

    def take_the_technique(self, device):
        # использовать тернанрный оператор не дает
        if device.price <= 4000:
            # если такой тип оргтехники уже добавляли в эконом
            if device.office_type in self.technique_econom:
                self.technique_econom[device.office_type] = self.technique_econom.get(device.office_type) + device.model_count
            else:
                self.technique_econom[device.office_type] = device.model_count
        else:
            # если такой тип оргтехники уже добавляли в премиум
            if device.office_type in self.technique:
                self.technique[device.office_type] = self.technique.get(device.office_type) + device.model_count
            else:
                self.technique[device.office_type] = device.model_count

    def get_the_technique(self, device, get_count: int = 0):
        if device in self.technique_econom.keys():
            if get_count <= self.technique_econom.get(device):
                self.technique_econom[device] = self.technique_econom.get(device) - get_count
            else:
                get_count -= self.technique_econom.get(device)
                self.technique_econom[device] = 0
            print("Эконом сегмент осталось:", self.technique_econom.get(device))
        if device in self.technique.keys():
            if get_count > self.technique.get(device):
                get_count -= self.technique_econom.get(device)
                self.technique_econom[device] = 0
                print(f"выдали все {device}, не хватает {get_count} шт.")
            else:
                self.technique[device] = self.technique.get(device) - get_count
            print("Премиум сегмент осталось:", self.technique[device])

    def __str__(self):
        all_device = OfficeEquipment()
        return f"На складе всего {all_device} устройств.\n" \
               f"Из них\nэконом класса: {'; '.join([f'{key}: {value}' for key, value in self.technique_econom.items()])}\n" \
               f"премиум класса: {'; '.join([f'{key}: {value}' for key, value in self.technique.items()])}\n"


class OfficeEquipment:

    __count_equipment: int = 0
    office_type = ""

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0):
        """
               name - название фирмы устройства
               price - цена
               number_of_lists - колчество листов в минуту
               count - количество устройств
        """
        OfficeEquipment.__count_equipment += count
        self.name = name
        self.model_count = count
        self.price = price
        self.number_of_lists = number_of_lists

    @abstractmethod
    def get_count(self) -> int:
        pass

    def __str__(self):
        return f"{self.__count_equipment}"


class Printer(OfficeEquipment):
    __count: int = 0

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0, *args):

        Printer.office_type = "Принтер"
        if name and price and number_of_lists and count:
            super().__init__(name, price, number_of_lists, count)

    @staticmethod
    def get_count() -> int:
        return Printer.__count

    def to_print(self):
        return f"{self.name} печатает со скоростью {self.number_of_lists} л/мин."


class Scaner(OfficeEquipment):
    __count: int = 0

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0, *args):
        Scaner.office_type = "Сканер"
        if name and price and number_of_lists and count:
            super().__init__(name, price, number_of_lists, count)

    @staticmethod
    def get_count() -> int:
        return Scaner.__count

    def to_scan(self):
        return f"{self.name} сканирует со скоростью {self.number_of_lists} л/мин."


class Xerox(OfficeEquipment):
    __count: int = 0

    def __init__(self, name: str = "", price: int = 0, number_of_lists: int = 0, count: int = 0, *args):
        Xerox.office_type = "Копировальный аппарат"
        if name and price and number_of_lists and count:
            super().__init__(name, price, number_of_lists, count)

    @staticmethod
    def get_count() -> int:
        return Xerox.__count

    def to_xerox(self):
        return f"{self.name} делает {self.number_of_lists} копий(и) в минуту."


def get_type_tehnics(message: str, range_if: int = 0, data_list: list = []):
    if data_list:
        for ind, el in enumerate(data_list):
            print(ind + 1, el.office_type)
    it = input(message)
    try:
        it = int(it)
    except ValueError:
        print("\033[31mВы ввели не число\033[0m")
        print("-"*25)
        it = get_type_tehnics("Попробуйте еще раз: ", range_if, data_list)
    else:
        while it not in range(1, range_if + 1):
            print("-" * 25)
            it = get_type_tehnics("\033[31mВы ввели не правильный индекс\033[0m\nПопробуйте еще раз: ", range_if, data_list)
    return it

sklad = Warehouse()

first_printer = Printer("LG", 5000, 18, 2)
sec_printer = Printer("Samsung", 5200, 22, 1)
sklad.take_the_technique(first_printer)
sklad.take_the_technique(sec_printer)

fist_scan = Scaner("HP", 3000, 6, 6)
sec_scan = Scaner("HP", 5700, 7, 3)
sklad.take_the_technique(fist_scan)
sklad.take_the_technique(sec_scan)

fist_xerox = Xerox("Xerox", 3000, 6, 10)
sec_xerox = Xerox("Dell", 4100, 7, 5)
sklad.take_the_technique(fist_xerox)
sklad.take_the_technique(sec_xerox)


features = {'название (модель)': '', 'цена': '', 'количество листов в минуту': '', 'количество устройств': ''}
org_tehnics = [Printer(), Scaner(), Xerox()]
while True:
    line = input('Для выхода из программы нажмите "Q", для запроса о количестве техники на складе "?", для продолжения "Enter": ')
    if line.upper() == 'Q':
        break
    elif line == "?":
        print(sklad)
    #*****************************
    line = get_type_tehnics("Желаете получить технику - '1', завезти на склад - '2'? ", 2)
    if line == 1:
        ind = get_type_tehnics("Укажите, какую технику желаете получить: ", len(org_tehnics), org_tehnics)
        user_get = input("Укажите количество: ")
        sklad.get_the_technique(org_tehnics[ind - 1].office_type, int(user_get))
        continue
    elif line == 2:
        ind = get_type_tehnics("Укажите, какую технику привезли: ", len(org_tehnics), org_tehnics)
        f_copy = features.copy()
        for f in features:
            pro = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
            f_copy[f] = int(pro) if f == 'цена' or f == 'количество листов в минуту' or\
                                    f == 'количество устройств' else pro  # Меняем тип числовых свойства
        if ind == 1:
            user_device = Printer(*list(f_copy.values()))
        elif ind == 2:
            user_device = Scaner(*list(f_copy.values()))
        else:
            user_device = Xerox(*list(f_copy.values()))
        sklad.take_the_technique(user_device)

