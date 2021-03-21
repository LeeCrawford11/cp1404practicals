"""
CP1404/CP5632 - Practical
Lee Crawford
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)
    random_score = random.randint(1,100)
    print(random_score)
    print(determine_grade(random_score))


def determine_grade(score):
    if 0 <= score <= 100:
        if score >= 90:
            score_statement = "Excellent"
        elif score >= 50:
            score_statement = "Pass"
        else:
            score_statement = "Bad"
        return score_statement
    else:
        return "Score outside limits"


main()

