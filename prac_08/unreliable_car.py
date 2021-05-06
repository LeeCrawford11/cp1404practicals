from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car"""

    def __init__(self, name="", fuel=0, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance
