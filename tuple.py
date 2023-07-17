course=("CSE","IT","MECH")
print(course)
print(type(course))
print(course[1])
print(course[-1])
print(course[0:2])
l1=[10,20,30]
print(l1)
course2=("HIST",["BBM","MBA"])
print(course2)
course2[1][1]="ENGLISH"
print(course2)
"""coursefull=course+course2
print(type(coursefull))
del coursefull
print(coursefull)"""
course_rep=("PHYSICS",)*4
print(type(course_rep))
print(course_rep)
print(course_rep.count("PHYSICS"))

for i in course:
    print(i)
for i,v in enumerate (course,start=1):
    print(i,v)
print(help(tuple))






