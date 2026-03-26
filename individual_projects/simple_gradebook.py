# NS 1st Simple Grade Book 
import csv

print("=====================================\n📚 SIMPLE GRADE BOOK 📚\n=====================================")
print("Welcome to the Class Grade Book!")
def main_menu():
    print("🎯 MAIN MENU:")
    print("\n1.Add New Student\n2.Add Grade to Student\n3.View Student Record\n4.View All Students\n5.Class Summary\n6.Exit")
    choice = input("Enter your choice (1-6):  ")
    if choice == "1":
        add_new_student()
    if choice == "2":
        add_grade()

def add_new_student():
    student_name = input("Enter Student name: ")
    student_id = input("Enter Student ID: ")
    print("✅ Student added successfully!")
    print(f"Name: {student_name}")
    print(f"ID: {student_id}")
    print(f"Grade: {grade}")
    new_row_data = [f'{student_name}', f'{student_id}', f'{grade}']
    with open('CSV\\students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_row_data)

def add_grade():
    id = input("Enter Student ID: ")
    grade = input("Enter grade(0-100): ")
    if grade == 95 < 100:
        print("Grade: A")
    if grade == 90 < 94:
        print("Grade: A-")
    if grade == 87 < 89:
        print("Grade: B+")
    if grade == 85 < 86:
        print("Grade: B")
    if grade == 80 < 84:
        print("Grade: B-")
    if grade == 77 < 79:
        print("Grade: C+")
    if grade == 75 < 76:
        print("Grade: C")
    if grade == 70 < 74:
        print("Grade: C-")
    if grade == 67 < 69:
        print("Grade: D+")
    if grade == 65 < 66:
        print("Grade: D")
    if grade == 60 < 64:
        print("Grade: D-")
    if grade == 0 < 59:
        print("Grade: F")


#def view_records():
     
#def view_students():


main_menu()