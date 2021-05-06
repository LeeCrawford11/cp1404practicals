from unreliable_car import UnreliableCar


def main():
    prius_taxi = UnreliableCar("Prius 1", 100, 50)
    for line in range(10):
        prius_taxi.drive(20)
        print(prius_taxi.odometer, prius_taxi.fuel)


main()
