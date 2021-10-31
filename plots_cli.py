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
                            userfile = string[1]
                            first_name= string[3]
                            last_name= string[2]
                            param = ["stu", r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv", "Elsawi", "Talaat"]
                            student_average(["stu", userfile, last_name,first_name])

                    except:
                        if user == "":
                            user = input("enter a command or 'quit' to quit")
                            quits()
            elif cmd == 'avg':
                    if len(string) != 3:
                        print('incorrect usage: avg <filename> <grade item>')
                    else:
                        userfile = string[1]
                        gradeitem = string[2]
                        print_average(["avg",userfile,gradeitem])

            else:
                print('invalid command')

def student_average(stu_string, plot):

    stu_string = ["stf",r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv"] as userfile:
    csv_reader = csv.reader(userfile)
    firstname = stu_string[2]
    lastname= stu_string[3]
    row = []
    for row in csv_reader:
        while firstname in row:
            if lastname in row:
                print(row)
                plotter.init("my graph", "X-axis", "Y-axis")
                plotter.new_series()
                for i in range(len(plot)):
                    plotter.add_data_point(plot[i])
                    plotter.plot()
                    plotter.plot()
                if plotter.plot() == True:
                    print('Plotting complete. (window may be hidden)')
                break
            elif plotter.plot() == False:
                print('Plot faild. (student not found)')
                break

                except:
             print('name not found in csv file')

           except:


      print('file not found')







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
