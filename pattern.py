"""no_of_rows=eval(input("Row :"))
for row in range(1,no_of_rows+1):
    for col in range(1,row+1):
        print("*",end="\t")
    print()"""

"""n=eval(input("Enter Number:"))
for i in range(0,n):
    for j in range(i,n):
        print("*",end=" ")
    print()"""

n=eval(input("Enter Number :"))
for row in range(0,n):
    for col in range(0,n+1):
        if(row<n-col):
            print(" ",end="  ")
        else:
            print("*",end="  ")
    print()