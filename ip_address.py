import re
def check(a):
    pattern=re.compile(r"(?:\b[0-1]?[0-9]?[0-9]?\b|\b[2]?[0-5]?[0-5]?\b).(?:\b[0-1]?[0-9]?[0-9]?\b|\b[2]?[0-5]?[0-5]?\b).(?:\b[0-1]?[0-9]?[0-9]?\b|\b[2]?[0-5]?[0-5]?\b).(?:\b[0-1]?[0-9]?[0-9]?\b|\b[2]?[0-5]?[0-5]?\b)")
    x=pattern.findall(a)
    if x:
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")
  
def main():
    ip=input("Enter the IPv4 address: ")
    check(ip)

main()