# 1- Create a Course class with attributes name and students (empty list at start)
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    # 2- Add a method to add a student to the list
    def add_student(self, student):
        self.students.append(student)
        print(f"{student} has been added to the course {self.name}.")

    # Method to display enrolled students
    def display_students(self):
        if self.students:
            print(f"Students enrolled in the course {self.name}:")
            for student in self.students:
                print(f"- {student}")
        else:
            print(f"No students are enrolled in the course {self.name} yet.")


# 3- Create a Course object, add students, and display them
course_1 = Course("Python")
course_1.add_student("Yahya")
course_1.add_student("Ali")
course_1.add_student("Sara")

course_1.display_students()
course_2 = Course("JavaScript")
course_2.add_student("Lina")   
course_2.display_students()