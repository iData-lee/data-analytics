student_name = 'Lisa Newnez'
student_major = 'HIST'

if student_major == 'BIOL':
    major_name = 'Biology'
    dept_office = 'Science Bldg, Romm 310'
elif student_major == 'CSCI':
    major_name = 'Computer Science' 
    dept_office = 'Sheppard Hall, Room 314'
elif student_major == 'ENG':
    major_name = 'English'
    dept_office = 'Kerr Hall, Room 201'
elif student_major == 'HIST':
    major_name = 'History'
    dept_office = 'Kerr Hall, Room 114'
elif student_major == 'MKT':
    major_name = 'Marketing'
    dept_office = 'Westly Hall, Room 310'
else:
    student_major == '<unknown>'
    major_name = ''
    dept_office = ''

print(f'Student: {student_name}')
print(f'Major: {major_name}')
print(f'Department Office: {dept_office}')