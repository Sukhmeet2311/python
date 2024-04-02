friends= [
    {"name": "Bob", "age": 24},
    {"name": "Adam", "age": 24},
    {"name": "Nishtha", "age": 24, "case" : "y"},
]
print (friends)
print (friends[0])
print (friends[2]["case"])
for friend in friends:
    print (friend)

student_attendance = {"dean" : "44", "nishtha" : "25"}
for student in student_attendance:
    print (student)

for student,attendance in student_attendance.items():
    print (student, attendance)    

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
items = list(my_dictionary.items())
print(items)