employee={"NAME":"Ram","EXP":6,"skill":("python","java")}
print(employee)
print(type(employee))
print(employee["NAME"])
#print(employee["EMAIL"])
print(employee.get("EMAIL","Sorry No Info"))
employee["EMAIL"]="ram@abc,com"
print(employee.get, "sorry wrong info")
print(employee.keys())
print(employee.values())
print(employee.items())
dev=("ram","sam","vino")
tec=("python","java","devops")
team=dict(zip(dev,tec))
print(team)
d2={k:v for k,v in zip(dev,tec)}
print(d2)
num=(10,20,30,35,40)
a,*b,c=num
print(a)
print(b)
print(c)