"""
CP1404/CP5632 - Practical
Lee Crawford
Temperature conversion
"""


def main():
    menu = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            input_string = "Celsius: "
            celsius_temp = get_temperature(input_string)
            conversion = celsius_to_fahrenheit(celsius_temp)
            print(conversion)
        elif choice == "F":
            input_string = "Fahrenheit: "
            fahrenheit_temp = get_temperature(input_string)
            conversion = fahrenheit_to_celsius(fahrenheit_temp)
            print(conversion)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return "Result: {:.2f} c".format(celsius)


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return "Result: {:.2f} f".format(fahrenheit)


def get_temperature(string):
    finished = False
    temperature = 0
    while not finished:
        try:
            temperature = float(input(string))
            finished = True
        except ValueError:
            print("Please enter a valid float.")
    return temperature


main()
