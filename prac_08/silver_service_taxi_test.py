"""
CP1404/CP5632 Practical
Silver service taxi test
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test cases for SilverServiceTaxi class"""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    limo = SilverServiceTaxi("Limo", 200, 2)
    limo.drive(18)
    print(limo)
    print("${:.2f}".format(limo.get_fare()))


main()
