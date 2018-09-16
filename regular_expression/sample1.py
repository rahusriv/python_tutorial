import re

p = re.compile("[a-z]+",re.IGNORECASE)

m = p.match("")
print(m)

m = p.match("tempo324") #always checks if a pattern matches at the start of the string
print(m)

print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.search("1234tempo657andd456")#Checks the complete string
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = p.findall("1234tempo657andd456") #return list of all the matches found
print(m)

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
