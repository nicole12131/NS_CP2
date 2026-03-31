# NS 1st
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # add a grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # calculate average
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # get letter grade
    def get_letter(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    # display student info
    def display(self):
        avg = self.get_average()
        if len(self.grades) == 0:
            print(f"{self.name} (ID: {self.student_id}) - No grades yet")
        else:
            print(f"{self.name} (ID: {self.student_id}) - Avg: {avg:.1f} ({self.get_letter()})")

class GradeBook:
    def __init__(self):
        self.students = []

    # add student
    def add_student(self, name, student_id):
        self.students.append(Student(name, student_id))

    # find student by ID
    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    # show all students
    def show_all(self):
        if len(self.students) == 0:
            print("No students found.")
        else:
            for s in self.students:
                s.display()

    # class summary
    def class_summary(self):
        if len(self.students) == 0:
            print("No students in class.")
            return

        total = 0
        count = 0

        for s in self.students:
            if len(s.grades) > 0:
                total += s.get_average()
                count += 1

        if count == 0:
            print("No grades available.")
        else:
            print(f"Class average: {total / count:.1f}")

# Main Program
book = GradeBook()

print("📚 SIMPLE GRADE BOOK 📚")

while True:
    print("\nMAIN MENU")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Student")
    print("4. View All Students")
    print("5. Class Summary")
    print("6. Exit")

    choice = input("Choose: ")

    # add student
    if choice == "1":
        name = input("Enter name: ")
        student_id = input("Enter ID: ")
        book.add_student(name, student_id)
        print("Student added!")

    # add grade
    elif choice == "2":
        student_id = input("Enter student ID: ")
        student = book.find_student(student_id)

        if student:
            try:
                grade = int(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    student.add_grade(grade)
                    print("Grade added!")
                else:
                    print("Grade must be 0-100.")
            except:
                print("Invalid input.")
        else:
            print("Student not found.")

    # view one student
    elif choice == "3":
        student_id = input("Enter student ID: ")
        student = book.find_student(student_id)

        if student:
            student.display()
        else:
            print("Student not found.")

    # view all
    elif choice == "4":
        book.show_all()

    # class summary
    elif choice == "5":
        book.class_summary()

    # exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
