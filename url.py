import re
def url(m):
    pattern=re.compile("https?:\/\/\S+")
    x=pattern.findall(m)
    if x:
        print("URLs are:",x)
    else:
        print("No URLs are present")
        
def main():
    text=input("Enter text:")
    url(text)

main()