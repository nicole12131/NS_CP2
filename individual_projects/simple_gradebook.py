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

with open("CSV\\students.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

def add_new_student():
    student_name = input("Enter Student name: ")
    student_id = input("Enter Student ID: ")
    print("✅ Student added successfully!")
    print(f"Name: {student_name}")
    print(f"ID: {student_id}")



main_menu()