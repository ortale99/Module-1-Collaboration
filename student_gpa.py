
# Name: Alejandra Ortega
# File: student_gpa.py
# Description: Checks if students qualify for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter student's last name (ZZZ to quit): ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "made the Dean's List!")

    if gpa >= 3.25:
        print(first_name, last_name, "made the Honor Roll!")

    if gpa < 3.25:
        print(first_name, last_name, "did not qualify.")

    print()

print("Program ended.")
