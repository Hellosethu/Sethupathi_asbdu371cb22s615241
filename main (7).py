class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def short_student(student_list):
    # Sort the student_list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    students = [
        Student("Alice", "A123", 3.8),
        Student("Bob", "B456", 3.9),
        Student("Charlie", "C789", 3.7),
        Student("David", "D101", 4.0),
    ]

    sorted_students = short_student(students)

    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")