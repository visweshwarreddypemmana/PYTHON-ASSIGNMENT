def get_student_marks():

    student_marks = {
        "Sai": 85,
        "Ram": 92,
        "Kiran": 78,
        "David": 95,
        "Rahul": 88
    }

    student_name = input("Enter the name of the student: ")

    student_name = student_name.strip()

    if student_name in student_marks:
        marks = student_marks[student_name]
        print(f"The marks for {student_name} are: {marks}")
    else:
        print(f"Sorry, '{student_name}' not found in the student records.")

get_student_marks()
