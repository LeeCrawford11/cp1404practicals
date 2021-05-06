"""
Lee Crawford
CP1404/CP5632 Practical - Do-from-scratch Exercises
Guitars
"""
from guitar import Guitars


def main():
    guitars = []
    finished = False
    print("My guitars!")
    while not finished:
        name = input("Name: ")
        print(name)
        if name == "":
            finished = True
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitars(name, year, cost)
        guitars.append(guitar)
    print("These are my guitars:")
    for index, guitar in enumerate(guitars, 1):
        print("Guitar {}: {}".format(index, guitar))


main()
