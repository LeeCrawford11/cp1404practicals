"""
Lee Crawford
CP1404/CP5632 Practical - Intermediate Exercises
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=0.0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {}, {}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
