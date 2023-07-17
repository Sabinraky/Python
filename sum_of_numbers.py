num=eval(input("Enter number :"))
sum=0
count=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    count+=1
    num=num//10
print("sum=",sum)
print(count)