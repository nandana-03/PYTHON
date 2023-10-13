import re
n=str(input("Enter the email id: "))
pattern=re.compile("[a-z][a-z0-9]*@(?!hotmail|yahoo)[a-z]+\.(?:com|in|org)")
r=re.findall(pattern,n)
if r:
    print("Valid email")
else:
    print("Invalid email")

