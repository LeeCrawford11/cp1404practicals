"""
CP1404/CP5632 Practical
Unreliable car class test
"""
from unreliable_car import UnreliableCar


def main():
    """Test cases for UnreliableCar class"""
    prius_taxi = UnreliableCar("Prius 1", 100, 50)
    for line in range(10):
        prius_taxi.drive(20)
        print(prius_taxi.odometer, prius_taxi.fuel)


main()
