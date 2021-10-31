import numpy as np
import csv
import plotter


def main():

              #quit function
        def quits():
                sure = input("are you sure?")
                while sure == 'y':
                    print('goodbye!')
                    return True
                while sure == 'Y':
                    print('goodbye!')
                    return True
                else:
                    return False
        def bye():
            user = input(">>")
            string = user.split()
            cmd = string[0]
            if cmd == "quit":
                    while quits() == True:
                        break
            elif cmd == 'stu':
                    try:
                        if len(string) != 4:
                            print('incorrect usage, "Usage: stu <filename> <last name> <first name>"')
                        else:


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     ('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
