class Student:
    def __init__(self, roll_no, name, age, grade):
        self.roll_no = 17
        self.name = 'rocky'
        self.age = 29
        self.grade = 'c'

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student_details(self):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        grade = input("Enter Grade: ")
        student = Student(roll_no, name, age, grade)
        self.students.append(student)
        print("Student details added successfully.")

    def display_student_details(self):
        print("Student Details:")
        for student in self.students:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Student found:")
                print(f"Roll No: {student.roll_no}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                return
        print("Student not found.")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student details deleted successfully.")
                return
        print("Student not found.")

    def update_student_details(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Enter new details:")
                student.name = input("Enter Name: ")
                student.age = int(input("Enter Age: "))
                student.grade = input("Enter Grade: ")
                print("Student details updated successfully.")
                return
        print("Student not found.")

    def menu(self):
        while True:
            print("\nStudent Management System Menu:")
            print("1. Accept Student Details")
            print("2. Display Student Details")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Update Student Details")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.accept_student_details()
            elif choice == 2:
                self.display_student_details()
            elif choice == 3:
                roll_no = int(input("Enter Roll No to search: "))
                self.search_student(roll_no)
            elif choice == 4:
                roll_no = int(input("Enter Roll No to delete: "))
                self.delete_student(roll_no)
            elif choice == 5:
                roll_no = int(input("Enter Roll No to update: "))
                self.update_student_details(roll_no)
            elif choice == 6:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()