    # students managment system

print("="*30)
print("students managment system")
print("="*30)

students=[
    {"id":101,"name":"Rahul","score":78},
    {"id":102,"name":"Raj","score":80},
    {"id":103,"name":"Ronak","score":75},
    {"id":104,"name":"Rohit","score":65}
    ]


print(students)  

print("="*30)
print("students Average score")
print("="*30)

sum=0

for student in students:
    sum+=student['score']

average = sum/4

print("\n Average student score:", average)
print(sum)


print("="*30)
print("add new student")
print("="*30)


students.append({
    "id":105,
    "name":"Riddhi",
    "score":80
    })

print(students)


print("="*30)
print("update students score")
print("="*30)


for student in students:
    if student['id'] == 102:
        student['score'] = 88

print(students)

print("="*40)
print("remove student from list")
print("="*40)

for student in students:
    if student['name'] == "ronk":
        student.remove(student)
        break;

print(student)


print("="*30)
print("update students score")
print("="*30)

for student in students:
  if student['score']>80:
      print(student['name'])


print("="*40)
print("Sort Decending")
print("="*40)


    
 













































