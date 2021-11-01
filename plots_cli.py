import numpy as np
import csv
import plotter


def main():

    command = input(">>")
    z = command.split()


    if (z[0] == "stu"):
        student_average(["stu", r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv", "Elsawi", "Talaat" , plotter.plot(trace_plot=True)])

    if (command == "avg"):
        print_average(["avg",r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv", 100])


    if (command == "cavg"):
          class_average()


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

def student_average(stu_string, plot, userfile):
  # calculates and plots
    stu_string = ["stf",r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv"]
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
                if  plotter.plot() == True:
                    print('Plotting complete. (window may be hidden)')
                break
            elif    plotter.plot() == False:
                print('Plot faild. (student not found)')
                break

        #try:

             #print('name not found in csv file')

   # try:


      #print('file not found')



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

def class_average():
    readdata = csv.reader(open(r"C:\Users\talaa\Downloads\GCIS.123.600-assignment2-sample (1).csv"))
    data = []

    for row in readdata:
        data.append(row)

    data.pop(0)

    q1= []

    for i in range(len(data)):
        q1.append(int(data[i]["my graph", "X-axis", "Y-axis"]))

    print ('Mean of my graph, X-axis, Y-axis :   ;(np.mean(q1))')

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
