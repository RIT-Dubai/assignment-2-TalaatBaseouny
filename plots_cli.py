import csv

import plotter


def main():

    command = input(">>")
    z = command.split()


    if (z[0] == "stu"):
        student_average(["stu", r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv", []] )

    if (command == "avg"):
        print_average(["avg",r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv", ])


    if (command == "cavg"):
          class_average(["cavg", r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv"] )


    if (command == "help"):
        help()

    if z[0] == str("quit"):
        quit()
        print("goodbye")


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

def bye(quits):
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

def student_average(stu_string):
    # calculates and plots the student average for one student only
    # a_string = "stu, filename, firstname, lastname"
   stu_string = ["stu",r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv", "Talaat", "Elsawi"]
   namefile = [1]
   if len(stu_string) != 4:
       print("Usage: stu <filename> <first name> <last name>")

   if (stu_string[1] == None):
         print("No such file: foo.csv")

# opening and reading the file
   else:
    try:
       with open(r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv") as namefile:
        csv_reader = csv.reader(namefile)
        fisrtname = stu_string[3]
        lastname = stu_string[2]
        row = []
        for row in csv_reader:
           while fisrtname in row:
               if lastname in row:
                   print(row)
                   print("Plot finished (window may be hidden).")
                   break

    except:
        print("Plot failed (no such student).")

def print_average(avg,):
     # prints the average
    csv=avg[1]
    f = open(csv)
    average=0
    Sum = 0
    column = 12
    for i in range(0,column):
        for n in range(i):
            n=float(n)
            Sum += n
        average = Sum / 12
        print(average)

def class_average(class_string, ):
  # plots multiple averages for multiple students
    class_string = ["cavg", "filename", ]
    with open(r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv") as namefile:
       csv_reader = csv.reader(namefile)
       print(csv_reader)
       fisrtname = class_string[0]
       lastname = class_string[0]
    row = []
    for row in csv_reader:
           while fisrtname in row:
               if lastname in row:
                   print(row)
                   plotter.init("my graph", "X-axis", "Y-axis")

    if len(class_string) != 2:
        print("Usage: cavg <filename>")

        try:
            if (class_string == True):
                print("Plot is finished (window may be hidden).")

            if (class_string[0] == False):
                print("Usage: cavg <filename>")
            if (class_string[1] == False):
                print("No such file: foo.csv")

        except:
            return


def help():
     # function to guide the user
    print("stu <filename> <first name> <last name> - plot student grades")
    print("cavg <filename> - plot class average")
    print("avg <filename> <number> - prints the average for the grade item")
    print("quit - quits")
    print("help - displays this message")

def students_average_plotting():
    plotter.init("my graph", "X-axis", "Y-axis")
    plotter.add_data_point(0.00)
    plotter.add_data_point(82)
    plotter.add_data_point(13.37)
    plotter.add_data_point(28.72)
    plotter.add_data_point(50.00)
    plotter.add_data_point(90.65)
    plotter.add_data_point(11.06)
    plotter.add_data_point(34.43)
    plotter.add_data_point(95)
    plotter.add_data_point(75)
    plotter.plot(trace_plot=True)
    input("input anything to exit")


def print_average_calculation():
    plotter.init("my graph", "x-axis","y-axis")
    plotter.plot(trace_plot=True)
    input("input anything to exit")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
