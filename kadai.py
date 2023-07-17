five_rupees=eval(input("Enter number of 5 ruppes :"))
one_rupees=eval(input("enter number of 1 ruppes :"))
total_value=eval(input("Enter total value :"))
if(total_value==0):
    five = total_value // five_rupees
    total_value = total_value - (5 * five)
    one = total_value // one_rupees
    total_value = total_value - (1 * one)
    print("Number of 5 rupees",five)
    print("Number of 2 rupees", one)
if(total_value!=0):
    five = total_value // five_rupees
    total_value = total_value - (5 * five)
    one = total_value // one_rupees
    total_value = total_value - (1 * one)
    print("Number of 5 rupees", five)
    print("Number of 2 rupees", one)







