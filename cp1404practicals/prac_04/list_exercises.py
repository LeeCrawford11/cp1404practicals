"""
Lee Crawford
CP1404/CP5632 Practical
Basic list operations
"""

# INPUT_TOTAL = 5
#
#
# def main():
#     number_count = 0
#     print("Please enter {} numbers".format(INPUT_TOTAL))
#     numbers = get_list_of_numbers(number_count)
#     display_list(numbers)
#     display_interesting_information(numbers)
#
#
# def get_list_of_numbers(number_count):
#     """Get a list of numbers from the user INPUT_TOTAL long"""
#     numbers = []
#     while number_count != INPUT_TOTAL:
#         number = int(input("Number: "))
#         numbers.append(number)
#         number_count += 1
#     return numbers
#
#
# def display_list(numbers):
#     """Print numbers from a list"""
#     for number in numbers:
#         print(number)
#
#
# def display_interesting_information(numbers):
#     """Print interesting information from a list of numbers"""
#     print("The first number is {}".format(numbers[0]))
#     print("The last number is {}".format(numbers[-1]))
#     print("The smallest number is {}".format(min(numbers)))
#     print("The largest number is {}".format(max(numbers)))
#     print("The average of the numbers is {}".format(sum(numbers)/INPUT_TOTAL))
#
#
# main()


def main():

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
    username = input("Enter your user name: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
