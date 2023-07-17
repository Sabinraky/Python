amt=eval(input("Enter the amount :"))
amt_2000=0
amt_500=0
amt_200=0
amt_100=0
amt_50=0
amt_20=0
amt_10=0
amt_5=0
amt_2=0
amt_1=0
if amt>=2000:
    amt_2000=amt//2000
    amt=amt-(amt_2000*2000)
    print("2000*",amt_2000,"=",amt_2000*2000)
if amt>=500:
    amt_500=amt//500
    amt=amt-(amt_500*500)
    print("500*",amt_500,"=",amt_500*500)
if amt>=200:
    amt_200=amt//200
    amt=amt-(amt_200*200)
    print("200*",amt_200,"=",amt_200*200)
if amt>=100:
    amt_100=amt//100
    amt=amt-(amt_100*100)
    print("100*",amt_100,"=",amt_100*100)
if amt>=50:
    amt_50=amt//50
    amt=amt-(amt_50*50)
    print("50*",amt_50,"=",amt50*50)
if amt>=20:
    amt_20=amt//20
    amt=amt-(amt_20*20)
    print("20*",amt_20,"=",amt_20*20)
if amt>=10:
    amt_10=amt//10
    amt=amt-(amt_10*10)
    print("10*",amt_10,"=",amt_10*10)
if amt>=5:
    amt_5=amt//5
    amt=amt-(amt_5*5)
    print("5*",amt_5,"=",amt_5*5)
if amt>=2:
    amt_2=amt//2
    amt=amt-(amt_2*2)
    print("2*",amt_2,"=",amt_2*2)
if amt>=1:
    amt_1=amt//1
    amt=amt-(amt_1*1)
    print("1*",amt_1,"=",amt_1*1)
total_notes=(amt_2000+amt_500+amt_200+amt_100+amt_50+amt_20+amt_10+amt_5+amt_2+amt_1)
print("Total number of Notes=",total_notes)

five_rupees = total_value // 5
    total_value = total_value - (5 * five_rupees)
    one_rupees = total_value // 1
    total_value = total_value - (1 * one_rupees)
    print("Number of 5 rupees", five_rupees)
    print("Number of 1 rupees", one_rupees)
    print("The value is -1")


