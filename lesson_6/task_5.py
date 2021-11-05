class Stationery:
    title: str
    _message = "Запуск отрисовки."

    def draw(self):
        print(self._message)


class Pen(Stationery):
    title = "Ручка"
    _message = f"{title} - пишет в тетрадке."

    def draw(self):
        print(self._message)


class Pencil(Stationery):
    title = "Карандаш"
    _message = f"{title} - пишет и можно стереть ластиком."

    def draw(self):
        print(self._message)


class Handle(Stationery):
    title = "Маркер"
    _message = f"{title} - пишет на доске и стирается губкой."

    def draw(self):
        print(self._message)


my_stationery = [Pen(), Pencil(), Handle()]

for item in my_stationery:
    item.draw()
