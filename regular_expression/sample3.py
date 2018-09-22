import re

#pattern =r"10.20.30.40";
pattern =r"([1][0])(\.)([2][0])(\.)([3][0])(\.)([1,2][0-9]*)";
p = re.compile(pattern,re.IGNORECASE)
email = input("Please enter ip address address:")

m = p.match(email)
if(m is None):
    print("No match found")
else:
    print("Match found")