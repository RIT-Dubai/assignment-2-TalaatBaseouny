import plots_cli

def test_student_average():
    "  Tests three command inputs and their expected output "

    args_true = ["stu", "points.csv", "Talaat", "Elsawi"]
    args_none = ["stu", "point.csv", "Kashyap", "kyle Bene"]
    args_false = ["stu", "points.csv", "Kashyap", "'kyle Bene"]
    assert plots_cli.student_average(args_true) == True
    assert plots_cli.student_average(args_none) == None
    assert plots_cli.student_average(args_false) == False



