"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
    print(os.getcwd())
    os.chdir('C:/Users/Lee/PycharmProjects/CP1404/prac_09/Lyrics')
    print(os.getcwd())
    new_file_name = [file for file in os.walk(".")]
    for index, name in enumerate(new_file_name):
        try:
            print(name)
        except FileExistsError:
            pass


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    try:
        if " " in filename:
            new_name = filename.replace(" ", "_")
    except UnboundLocalError:
        pass
    for index, char in enumerate(filename):
        if char.islower() and filename[index].isupper():
            new_name = filename[:index+1] + " " + filename[index:]
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files


main()
# demo_walk()