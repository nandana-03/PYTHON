import re
dob=input("Enter the date of birth in MM/DD/YYYY format: ")
pattern=re.compile(r"\b(?:01|02|03|04|05|06|07|08|09|10|11|12)/(?:[0-2][0-9]|[3][0-1])/[0-9][0-9][0-9][0-9]\b")
n=re.findall(pattern,dob)
if n:
    print("Date in required format")
else:
    print("Date not in required format")