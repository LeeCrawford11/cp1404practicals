""" 
Lee Crawford
CP1404/CP5632 Practical - Do-from-scratch Exercises
"""


class Guitars:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost
        self.vintage_string = " (vintage)" if self.is_vintage() else ""

    def __str__(self):
        return "{} ({}), worth ${:.2f}{}".format(self.name, self.year, self.cost, self.vintage_string)

    def get_age(self):
        """Gets age of guitar"""
        age = 2021 - self.year
        return age

    def is_vintage(self):
        """Checks if age is equal or more than 50"""
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
