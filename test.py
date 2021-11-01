import plots_cli

def test_student_average():
    "  Tests three command inputs and their expected output "

    args_true = ["stu", "points.csv", "Talaat", "Elsawi"]
    args_none = ["stu", "point.csv", "Kashyap", "kyle Bene"]
    args_false = ["stu", "points.csv", "Kashyap", "'kyle Bene"]
    assert plots_cli.student_average(args_true) == True
    assert plots_cli.student_average(args_none) == None
    assert plots_cli.student_average(args_false) == False


def test_print_average():
    "calculates hard coded values"

    args = ["avg", "points.csv", 1]
    args_fail = ["avg", "points.csv", 11]
    data = [12.67, 16.67, 14.0, 16.67, 16.0, 0, 8.0, 18.67, 14.7, 14.67, 10.0, 12.67, 13.33, 8.67, 15.33, 15.33, 14.67, 13.33, 7.33, 16.00, 17.33, 19.33, 15.33, 0, 6.67, 15.33, 18.0, 16.67, 13.33, 15.33, 15.33, 16.0, 14.0]
    avg = sum(data) / len(data)
    assert plots_cli.print_average(args)[0] == avg
    assert plots_cli.print_average(args_fail) == -1
