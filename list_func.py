course=["MECH","ECE","IT","CSE"]
"""print(course)
print(len(course))
print(type(course))
print(course[0])
print(course[-1])
#print(course[4])
print(course[0:2])
print(course[:2])
print(course[2:])
print(course[1:2])
course.append("EEE")
print(course)
course.insert(2,"BIOMED")
print(course)
course_2=["EI","FOODTECH"]
course.append(course_2)
print(course)
print(course[6][0])
course.pop()
print(course)
course.extend(course_2)
print(course)
course.reverse()
print(course)
course.sort()
print(course)
course.sort(reverse=True)
print(course)"""
num=[30,50,60,10]
"""num.sort()
print(num)
num.sort(reverse=True)
print(num)"""
sortedlist=sorted(num)
print(sortedlist)
print(num)
print(min(num))
print(max(num))
print(sum(num))
print(course.index("MECH"))
#print(course.index("BBM"))
print("BBM" in course)
print("BBM" not in course)
for i in course:
    print(i)
for i,v in enumerate(course):
    print(i,v)
for i,v in enumerate(course,start=100000000):
    print(i,v)
course_str='-'.join(course)
print(course_str)
print(type(course_str))
course_list=(course_str.split(','))
print(course_list)
print(type(course_list))
print(help(tuple))





