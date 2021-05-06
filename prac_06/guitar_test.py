from guitar import Guitars


def main():
    guitar = Guitars("Gibson L-5 CES", 1922, 16035.4)
    another_guitar = Guitars("Another Guitar", 2013, 2255.3)
    third_guitar = Guitars("Third Guitar", 1971, 12345)
    print("{} get_age() - Expected 99. Got {}".format(guitar.name, guitar.get_age()))
    print("{} get_age() - Expected 8. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} get_age() - Expected 99. Got {}".format(third_guitar.name, third_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))
    print("{} is_vintage() - Expected True. Got {}".format(third_guitar.name, third_guitar.is_vintage()))


main()
