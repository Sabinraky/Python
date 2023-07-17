"""def sum_fun():
     a,b=10,20
     print("inside sum fun",a+b)
def dif_fun():
    a,b=10,20
    print("Inside th function",b-a)
sum_fun()
dif_fun()"""

#FUNCTION_SIGNATURE


def sum(num,num2):
    a,b=num,num2
    print("Inside fun",a+b)

def sub(num,num2=0):
    a,b=num,num2
    print("Inside fun",b-a)

sub(10)
sub(200,300)


"""def sum(x,y):
    a,b=10,20
    print("sum =",x+y)
def dif(x,y):
    a,b=x,y
    print("diffrence =",y-x)

a=int(input("A value"))
b=int(input("B value"))
sum(a,b)
dif(a,b)"""