start_val=eval(input("Enter start value :"))
end_value=eval(input("Enter end value :"))
if(start_val%2==0):
    print("even")
    for i in range(start_val,end_value,2):
        print(i,end="\t")
    print("odd")
    for i in range(start_val+1,end_value,2):
        print(i,end="\t")
elif(start_val%2!=0):
    print("even")
    for i in range (start_val+1,end_value,2):
        print(i,end="\t")
    print("odd")
    for i in range(start_val,end_value,2):
        print(i,end="\t")
else:
    print("even")
    for i in range (start_val,end_value,2):
        print(i,end="\t")
    print("odd")
    for i in range(start_val+1,end_value,2):
        print(i,end="\t")