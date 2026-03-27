#program that record, update, and delete student student grades.
#handle exception like invalids student id, empty grade input , type missmatch


class InvalidStudentIDError(Exception):
    pass

class EmptyGradeError(Exception):
    pass

class TypeMismatchError(Exception):
    pass


class StudentGradeSystem:
    def __init__(self):
        self.students = {}  

    
    def record_grade(self, student_id, grade):
        try:
            if student_id not in self.students:
                raise InvalidStudentIDError("Student ID does not exist.")

            if grade == "":
                raise EmptyGradeError("Grade cannot be empty.")

            if not isinstance(grade, (int, float)):
                raise TypeMismatchError("Grade must be a number.")

            self.students[student_id] = grade
            print("Grade recorded successfully.")

        except Exception as e:
            print("Error:", e)

    
    def add_student(self, student_id):
        self.students[student_id] = None
        print("Student added successfully.")

    
    def update_grade(self, student_id, grade):
        try:
            if student_id not in self.students:
                raise InvalidStudentIDError("Invalid Student ID.")

            if grade == "":
                raise EmptyGradeError("Grade cannot be empty.")

            if not isinstance(grade, (int, float)):
                raise TypeMismatchError("Grade must be numeric.")

            self.students[student_id] = grade
            print("Grade updated successfully.")

        except Exception as e:
            print("Error:", e)

    
    def delete_student(self, student_id):
        try:
            if student_id not in self.students:
                raise InvalidStudentIDError("Student ID not found.")

            del self.students[student_id]
            print("Student deleted successfully.")

        except Exception as e:
            print("Error:", e)

    
    def display(self):
        print("\nStudent Records:")
        for sid, grade in self.students.items():
            print("ID:", sid, "Grade:", grade)



system = StudentGradeSystem()

system.add_student("S101")
system.add_student("S102")

system.record_grade("S101", 85)
system.update_grade("S101", 90)

system.delete_student("S102")

system.display()