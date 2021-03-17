"""
Lee Crawford
CP1404
prac 3
password_check
"""


minimum_length = 4
password = input("please enter your password: ")
while len(password) < minimum_length:
    print(f"Password must be at least {minimum_length} character/s long")
    password = input("please enter your password: ")
print("*" * len(password))