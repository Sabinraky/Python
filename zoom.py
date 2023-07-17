number=eval(input("Enter the number :"))
if(number%3==0 and number%5==0):
    print("Zoom")
elif(number%3==0):
    print("Zip")
elif(number%5==0):
    print("Zap")
else:
    print("Invalid Number")