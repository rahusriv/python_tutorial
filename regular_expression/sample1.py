import re

pattern =r"([a-z]{1})([a-z,0-9,\_,\-]*)([@])([a-z]+)(\.)([a-z]+)";
p = re.compile(pattern,re.MULTILINE)
email = input("Please enter an email address:")

m = p.match(email)
print(m)

print(m.group())
print(m.start())
print(m.end())
print(m.span())


print("*"*50)

p = re.compile(r"[a-z]+",re.IGNORECASE)
#p = re.compile(r"([a-z]+)|([1-9]+)",re.IGNORECASE)

m = p.match("")
print(m)

print("*"*50)

m = p.match("tempo324") #always checks if a pattern matches at the start of the string
#m = p.match("1234asd")
print(m)

print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("*"*50)
print("Search function")
m = p.search("1234tempo657andd456")#Checks the complete string
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("*"*50)

m = p.findall("1234tempo657andd456a56vggg7889nbsafsfkj5") #return list of all the matches found
print(m)

print("*"*50)

iter = p.finditer("1234tempo657andd456")
for match in iter:
    print(match.group()+" "+str(match.span()))

#Split string based on a pattern
m = p.split("1234tempo657andd456")
print(m)

p = re.compile(r'\W+')
para = input("Plearse input a paragraph:")
m = p.split(para)
print(m)

#print("My name is \n rahul")
#print(r"My name is \n rahul")
