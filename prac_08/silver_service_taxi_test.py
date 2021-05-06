from silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    limo = SilverServiceTaxi("Limo", 200, 2)
    limo.drive(18)
    print(limo)
    print("${:.2f}".format(limo.get_fare()))


main()
