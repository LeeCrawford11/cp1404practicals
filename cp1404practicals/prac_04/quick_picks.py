"""
Lee Crawford
CP1404/CP5632 Practical
Quick Picks
"""
import random
NUMBER_AMOUNT = 6
MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1


def main():
    quick_picks_amount = int(input("How many quick picks? "))
    for index in range(quick_picks_amount):
        printed_numbers = 0
        numbers = []
        while printed_numbers != NUMBER_AMOUNT:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if random_number not in numbers:
                numbers.append(random_number, )
                printed_numbers += 1
        numbers.sort()
        for number in numbers:
            print("{:>2}".format(str(number)), end=" ")
        print()


main()

