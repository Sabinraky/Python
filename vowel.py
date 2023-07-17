"""vowel_count=0
consonant_count=0
word=input("Enter word :")
for i in word:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'  ):
        vowel_count+=1
    else:
        consonant_count+=1
print("VOWEL :",vowel_count)
print("CONSONANT :",consonant_count)
print(i)"""

"""even_list=list()
odd_list=list()
count=0
word=input("Enter word :")
for i in word:
    if(count%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
    count+=1
print(even_list)
print(odd_list)"""

word=input("Enter :")
search=input("Search :")
count=0
for i in word:
    if(i==search):
        print(count)
    count+=1

