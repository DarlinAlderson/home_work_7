"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time
import colorama


class TrafficLight:
    __color = colorama.Fore.RED

    def running(self):
        print(self.__color + 'Красный')
        time.sleep(7)
        self.__color = colorama.Fore.YELLOW
        print(self.__color + 'Желтый')
        time.sleep(2)
        self.__color = colorama.Fore.GREEN
        print(self.__color + 'Зеленый')
        time.sleep(5)


colorama.init()
traffic_light_1 = TrafficLight()
traffic_light_1.running()
