"""
CP1404/CP5632 Practical
Unreliable car class
"""
from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability"""

    def __init__(self, name="", fuel=0, reliability=0.0):
        """Initialise a UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but determine if UnreliableCar is reliable enough as well."""
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
        else:
            distance = 0
        return distance
