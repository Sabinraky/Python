class Employee:
    #constructor_creation
    def __init__(self,name,pay,empid):
        self.name = name
        self.pay = pay
        self.empid = empid
    def display(self):
        print(self.name)
        print(self.pay)
        print(self.empid)
emp1=Employee("Rakesh",30000,101)
"""emp1.name="Rakesh"
emp1.pay=30000
emp1.empid=101
"""
emp1.display()
print()
emp2=Employee("Raky",50000,102)
emp2.name="Raky"
emp2.pay=50000
emp2.empid=102
emp2.display()


