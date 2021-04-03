"""
Lee Crawford
CP1404/CP5632 Practical
emails
"""

USERS = {}


def main():
    email = input("Email: ")
    while email != "":
        name_and_email = email.split("@")
        USERS[email] = return_name_from_email(name_and_email)
        print("Is your name {}?".format(USERS[email]).title(), end="")
        answer = input(" (Y/n) ").lower()
        if answer == "n" or answer == "no":
            USERS[email] = input("Name: ")
        email = input("Email: ")
    for key, name in USERS.items():
        print("{} ({})".format(name, key))


def return_name_from_email(name_and_email):
    """check if names separated by '.' then return string"""
    if "." in name_and_email[0]:
        names = name_and_email[0].split(".")
        user_name = "{} {}".format(names[0], names[1])
    else:
        user_name = name_and_email[0]
    return user_name


main()
