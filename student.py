class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def setGrades(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def printGrades(self):
        print(f"学生{self.name}(学号{self.id})的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]:.2f}分")

