# Simple Student Management System

students = []  # List to store student information (tuples)
courses = set()  # Set to store unique course names
grades = {}  # Dictionary to store grades for each student

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_id = input("Enter student ID: ")
    students.append((student_id, name, age))
    grades[student_id] = {}
    print(f"Student {name} added successfully.")

def add_course():
    course = input("Enter course name: ")
    courses.add(course)
    print(f"Course '{course}' added successfully.")

def assign_grade():
    student_id = input("Enter student ID: ")
    course = input("Enter course name: ")
    grade = float(input("Enter grade: "))
    if student_id in grades and course in courses:
        grades[student_id][course] = grade
        print(f"Grade {grade} assigned to student {student_id} for course '{course}'.")
    else:
        print("Error: Student ID or course not found.")

def display_info():
    print("\nStudents:", students)
    print("Courses:", courses)
    print("Grades:", grades)

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Assign Grade")
        print("4. Display All Info")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            assign_grade()
        elif choice == '4':
            display_info()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()