import re
n=input("Enter the phone number: ")
pattern=re.compile(r"\b\+?\d{1,3}\s\d{6,10}\b|\b\d{6,10}\b")
r=re.findall(pattern,n)
if not r:
    print("Invalid phone number")
else:
    print("Valid phone number")
