# 1. Класс автомобиль
# Реализовать класс автомобиль с полями: объем бака, количество
# бензина, текущий расход бензина(?), текущий объем бензина и скорость движения.
# Реализовать методы: старт, разгон, торможение и остановка. Задать таблицу участков дороги, содержащую
# протяженность и ограничение максимальной скорости на каждом участке, общая длина дороги – 50 км. Длина отдельного
# участка от 2 до 5 км. Задать таблицу зависимости расхода топлива от скорости автомобиля. Проехать по участку 30 км.
# Определить время поездки и общий расход топлива. Примечание: автомобиль движется с максимально допустимой скоростью
# на данном участке. Если скорость движения на участке не ограничена – с максимально-возможной конструктивной скоростью.
# Решение предоставить в виде работающего примера вместе с обеими таблицами данных. Дополнительно: реализовать
# метод переключения передач.
# В этом случае минимальная и максимальная скорости движения, а также расход топлива зависят от текущей передачи.
# Передачи могут переключаться последовательно
# в порядке возрастания при ускорении или при соответствии скорости движения при уменьшении скорости.

class MyCar():
    def __init__(self, max_petrol_volume, current_petrol_volume, max_speed, current_speed, current_consumption,
                 start_time, stop_time, road_time):
        self.max_petrol_volume = max_petrol_volume
        self.current_petrol_volume = current_petrol_volume
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.current_consumption = current_consumption
        self.start_time = start_time
        self.stop_time = stop_time
        self.road_time = road_time


    def calculate_total_time(self):
        total_time = self.start_time + self.road_time + self.stop_time
        print("Общее время в пути (с учетом времени на разгорев и останов) составило (мин): " + str(round(total_time, 2)))


    def get_current_consumption(self):
        print("Расход бензина к настоящему моменту составил (л): " + str(round(self.current_consumption, 3)))

    def get_current_petrol_volume(self):
        self.current_petrol_volume -= self.current_consumption
        print("Объем бензина в баке к настоящему моменту составил (л): " + str(round(self.current_petrol_volume, 3)))

    def start(self):
        self.current_consumption += 0.05

    def stop(self):
        self.current_consumption += 0.025
        self.current_speed = 0

    def func(self, road_number, speed_dict, consumption_dict, n, distance=0):
        for key in road_number.keys():
            if distance < n:
                distance += road_number[key]
                if speed_dict[key] > self.max_speed:
                    self.current_speed = self.max_speed
                else:
                    self.current_speed = speed_dict[key]
                self.road_time += (road_number[key]/self.current_speed)*60
                self.current_consumption += consumption_dict[self.current_speed]*road_number[key]/100
        print("Пройденное расстояние к настоящему моменту составило (км): " + str(distance))


road_number = {1: 2, 2: 3, 3: 5, 4: 5, 5: 5, 6: 4, 7: 4, 8: 2, 9: 5, 10: 5, 11: 3, 12: 5, 13: 2}
speed_dict = {1: 10, 2: 20, 3: 40, 4: 60, 5: 40, 6: 90, 7: 120, 8: 90, 9: 40, 10: 70, 11: 50, 12: 20, 13: 5}
consumption_dict = {10: 10, 20: 9.5, 30: 9, 40: 8.5, 50: 8, 60: 7.5, 70: 7, 80: 6.5, 90: 6, 100: 5.5, 110: 5}

myCar = MyCar(50, 35, 110, 0, 0, 2, 0.5, 0)
myCar.start()
myCar.func(road_number, speed_dict, consumption_dict, 30)
myCar.stop()

myCar.get_current_consumption()
myCar.get_current_petrol_volume()
myCar.calculate_total_time()