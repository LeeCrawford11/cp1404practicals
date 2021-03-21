"""
Lee Crawford
CP1404
prac 3
password_check
"""


def main():
    minimum_length = 4
    password = get_password(minimum_length)
    print_number_of_astericks(password)


def print_number_of_astericks(password):
    print("*" * len(password))


def get_password(minimum_length):
    password = input("please enter your password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} character/s long")
        password = input("please enter your password: ")
    return password


main()
