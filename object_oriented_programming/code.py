class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90,83,95)

    def average(self):
        return (sum(self.grades)/len(self.grades))

student= Student()        
print(student.name)
print(student.average())