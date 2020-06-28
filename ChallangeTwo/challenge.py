
class Car:
    def __init__(self):
        self._speed = 0
        self._star_car = False

    def start_car(self):
        if self._star_car:
            raise Exception("The car is already on.")
        self._star_car = True

    def turn_off_car(self):
        self._star_car = False

    def add_speed(self):
        if self._speed + 5 >= 240:
            self._speed = 240
        else:
            self._speed += 5

    def remove_speed(self):
        if self._speed - 5 <= 0:
            self._speed = 0
        else:
            self._speed -= 5

    def current_speed(self):
        return self._speed

    def stop(self):
        self._speed = 0

    def car_status(self):
        return self._star_car
