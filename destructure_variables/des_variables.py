x= 5,11 # tuple by default
print (x)


student_attendance = {"dean" : "44", "nishtha" : "25"}
print(student_attendance)
print(list(student_attendance.items()))
for student,attendance in student_attendance.items():
    print (f"{student}: {attendance}")

people = [("Sukhmeet", "34","Architect"), ("Nishtha","27","Designer")]    
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

test=[1,"Sukh", "Meet"]
_, name,last_name =test
print(name)
head,*tail = [1,2,3,4,5]
print(head)
print(tail)
print(*tail)