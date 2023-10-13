import re
def extract(x):
    pattern=re.compile("[0-9]+")
    n=pattern.findall(x)
    if n:
        print(f"Numbers are {n}")
    else:
        print("Numbers are not present in the text")
def main():
    txt=input("Enter the text:")
    extract(txt)
main()