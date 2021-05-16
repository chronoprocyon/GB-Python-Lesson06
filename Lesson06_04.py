"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула в следующем направлении: {direction}")

    def showspeed(self):
        print(f"Текущая скорость {self.speed}")


class TownCar(Car):
    doors_count = 4
    wheels_size = 19
    is_police = False

    def showspeed(self):
        if self.speed > 60:
            print("Вы превысили допустимую скорость!")
        else:
            print(f"Текущая скорость {self.speed}")


class SportCar(Car):
    max_speed = 300
    doors_count = 2
    is_police = False


class WorkCar(Car):
    wheels_count = 8
    is_police = False

    def showspeed(self):
        if self.speed > 40:
            print("Вы превысили допустимую скорость!")
        else:
            print(f"Текущая скорость {self.speed}")


class PoliceCar(Car):
    police_siren = True
    is_police = True


car_1 = TownCar(100, "White", "Honda")
car_1.showspeed()

car_2 = SportCar(100, "Red", "Porsche")
car_2.showspeed()

car_3 = WorkCar(30, "Black", "Hitachi")
car_3.showspeed()

print(SportCar.doors_count)

car_1.go()
car_1.stop()
car_1.turn("Left")
