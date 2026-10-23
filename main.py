class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100")
        self.marks.append(mark)
    def total(self):
        return sum(self.marks)
    def average(self):
        return self.total() / len(self.marks)
    def result(self):
        if self.average() >= 40:
            return "Pass"
        else:
            return "Fail"
    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Average:", round(self.average(),2))
        print("Result:", self.result())
students = []
students_count = int(input("Students count: "))
subjects_count = int(input("Subjects count: "))
for i in range(students_count):
    name = input(f"Enter student {i + 1} name: ")
    student = Student(name)
    for j in range(subjects_count):
        while True:
            try:
                student_marks = int(input(f"Enter marks for subject {j + 1}: "))
                student.add_mark(student_marks)
                break
            except ValueError as e:
                print("Invalid:", e)
                print("Please enter the mark again.")
    students.append(student)
for student in students:
student.show()