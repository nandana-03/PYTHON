import re
hash=input("Enter the sentence:")
pattern=re.compile("(#\w+)")
x=re.findall(pattern,hash)
print("Hashtags: ",x)