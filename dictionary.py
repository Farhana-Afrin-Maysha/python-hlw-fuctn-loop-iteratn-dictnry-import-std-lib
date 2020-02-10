student = {'name': 'Farhana', 'age':26, 'courses':['Math','ComSci']}

print(student.get('phone', 'Not Found'))
student['name'] = 'Maysha'
student.update({'phone':'57905-5678', 'name':'Maysha'})
print(student)

del student['age']
print(student)
for key, value in student.items():
  print(key , value)
