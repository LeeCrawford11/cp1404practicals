"""
Lee Crawford
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print_subject_details(data)


def get_data():
    parts_list = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts_list.append(parts)
    return parts_list
    input_file.close()


def print_subject_details(details):
    """take a list of lists and print them formatted within their sub-lists"""
    for detail in  details:
        current_list = detail
        print("{} is taught by {:12} and has {:>3} students".format(detail[0], detail[1], detail[2]))


main()
