"""l1=(1,2,3,4,5,6,7,8,9,10)
print(l1)
l2=list()
for i in range(1,11,):
    l2.append(i)

print(l2)
l3=[i for i in range(1,11)]
print(l3)"""

l1=[1,2,3,4,5,6,7,8,9,10]

l2=list()
for i in range (1,31):
     if(i%2==0):
         if(i%5==0):
             l2.append(i)
print(l2)

l3=[i for i in range (1,11) if(i%2==0) if(i%5==0)]
print(l3)
