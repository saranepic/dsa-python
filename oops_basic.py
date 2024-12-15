class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_students(self,student):
        if len(self.students) < self.max_students: 
            self.students.append(student)
            return True
        return False
    def get_average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)
    

s1=Student("Saran",24,90)
s2=Student("Kumar",21,78)
s3=Student("Singa",24,92)
c1=Course("Computer Science",2)
c1.add_students(s1)
c1.add_students(s2)
print(c1.students)
print(c1.get_average())
