import time


class TrafficLight:
    __color: str
    __timing: dict

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 7):
        self.__color_dict = {"red": "\033[31m", "yellow": "\033[33m", "green": "\033[32m"}
        self.__timing = {"\033[31m": red_time, "\033[33m": yellow_time, "\033[32m": green_time}

    def __repr__(self):
        return f"{self.__color}Горит {self.__color}"

    def running(self, color: str):

        # если такого цвета нет
        if not color in self.__color_dict.keys():
            print("Нет такого сигнала светофора")
            exit()
        # если цвет верный

        ind = list(self.__color_dict.keys()).index(color)

        for i in range(ind, len(self.__color_dict.keys())):
            self.__color = list(self.__color_dict.values())[i]
            timer = self.__timing[self.__color]
            for sec in range(1, timer + 1):
                print(f"{self} [{sec}]", end=" ")
                time.sleep(1)
            print()

"""Вариант решения без ввода цвета
         for k, v in self.__timing.items():
             Присваиваю self.__color = k, чтоб задействовть __repr__, можно было обойтись без этого
             self.__color = k
             for i in range(1, v + 1):
                 print(f"{self} [{i}]", end=" ")
                 time.sleep(1)
             print()
"""

try:
    my_light = TrafficLight(7, 2, 8)
    my_light.running("green")
except KeyboardInterrupt:
    print("Exit!")

