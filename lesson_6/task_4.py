class Car:
    speed: float
    color: str
    name: str
    is_police: bool = False
    state: bool = False

    def __init__(self, speed, color, name) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        if self.state:
            return f"{self.name} уже едет"
        else:
            self.state = True
            return f"{self.name} начала движение"

    def stop(self):
        if not self.state:
            return f"{self.name} уже остановлена"
        else:
            self.state = False
            return f"{self.name} остановилась"

    def turn(self, direction):
        if self.state:
            return f"{self.name} повернула {direction} и движется со скоростью {self.speed}"

    def show_speed(self):
        return f"{self.name}: скорость {self.speed} км/ч"


class TownCar(Car):
    def show_speed(self):
        print("Скорость превышена!" if self.speed > 60 else super().show_speed())


class SportCar(Car):
    def show_speed(self):
        print("Слишком медленно!" if self.speed < 100 else f"Текущая скорость {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        print("Скорость превышена!" if self.speed > 40 else super().show_speed())


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(240, 'red', 'Audi'),
    TownCar(180, 'silver', 'Kia'),
    WorkCar(80, 'white', 'Golf'),
    PoliceCar(170, 'black', 'Ford'),
]

print(cars[0].go())
print(cars[0].turn("направо"))
print(cars[0].stop())

for car in cars:
    car.show_speed()
