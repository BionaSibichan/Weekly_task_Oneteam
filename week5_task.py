from abc import ABC, abstractmethod

class Evaluation(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age


class Student(Person, Evaluation):
    total_students = 0

    def __init__(self, name, age, roll, m1, m2, m3):
        Person.__init__(self, name, age)
        self.roll = roll
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        Student.total_students += 1

    def total_marks(self):
        t = self.m1 + self.m2 + self.m3
        return t

    def average_marks(self):
        avg = self.total_marks()/3
        return avg

    def calculate_grade(self):
        avg = self.average_marks()
        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=60:
            return "C"
        else:
            return "D"

    def display(self):
        print("Name:",self.get_name())
        print("Age:",self.get_age())
        print("Roll No:",self.roll)
        print("Marks:",self.m1,self.m2,self.m3)
        print("Total:",self.total_marks())
        print("Avg:",self.average_marks())
        print("Grade:",self.calculate_grade())

    def __gt__(self,other):
        return self.total_marks()>other.total_marks()
    def __lt__(self,other):
        return self.total_marks()<other.total_marks()

    @staticmethod
    def validate_marks(mark):
        if mark<0 or mark>100:
            return False
        return True

    @classmethod
    def show_total_students(cls):
        print("Total students created:",cls.total_students)


class Sports:
    def __init__(self,sports_score):
        self.sports_score = sports_score
    def display_sports(self):
        print("Sports Score:",self.sports_score)


class Result(Student,Sports):
    def __init__(self,name,age,roll,m1,m2,m3,sports_score):
        Student.__init__(self,name,age,roll,m1,m2,m3)
        Sports.__init__(self,sports_score)

    def final_score(self):
        f = self.total_marks()+self.sports_score
        return f

    def display_result(self):
        self.display()
        self.display_sports()
        print("Final Scor:",self.final_score())


student_list = []
n = int(input("Enter number of students: "))
i=0
while i<n:
    print("\nEnter details of student",i+1)
    name = input("Name: ")
    age = int(input("Age: "))
    roll = int(input("Roll Number: "))

    m1 = int(input("Marks in Subject 1: "))
    while Student.validate_marks(m1)==False:
        print("Invalid marks")
        m1 = int(input("Marks in Subject 1: "))

    m2 = int(input("Marks in Subject 2: "))
    while Student.validate_marks(m2)==False:
        print("Invalid marks")
        m2 = int(input("Marks in Subject 2: "))

    m3 = int(input("Marks in Subject 3: "))
    while Student.validate_marks(m3)==False:
        print("Invalid marks")
        m3 = int(input("Marks in Subject 3: "))

    sports_score = int(input("Sports Score: "))

    s = Result(name,age,roll,m1,m2,m3,sports_score)
    student_list.append(s)
    i=i+1


print("\nStudent Details")
for s in student_list:
    s.display_result()


for i in range(len(student_list)):
    for j in range(len(student_list)-i-1):
        if student_list[j]<student_list[j+1]:
            temp = student_list[j]
            student_list[j] = student_list[j+1]
            student_list[j+1] = temp


print("\nRank List")
rank=1
for s in student_list:
    print("Rank",rank,"-",s.get_name(),"- Total Marks:",s.total_marks())
    rank=rank+1

print()
Student.show_total_students()