str1=input("Enter a string: ")
cnt=0
ccnt=0
for i in str1:
    if i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=='O' or i=='U':
        cnt+=1
    elif((i>='a' and i<='z') or (i>='A' and i<='Z')):
        ccnt+=1
print(f"Number of vowels are {cnt}")
print(f"Number of consonants are {ccnt}")