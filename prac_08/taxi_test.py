from taxi import Taxi


def main():
    prius_taxi = Taxi("Prius 1", 100)
    prius_taxi.drive(20)
    print(prius_taxi, prius_taxi.get_fare())
    prius_taxi.start_fare()
    prius_taxi.drive(100)
    print(print(prius_taxi, prius_taxi.get_fare()))


main()
