
#iterators in python

mystring = "123456"

my_iterator = iter(mystring)
print(next(my_iterator))
next(my_iterator)
next(my_iterator)
next(my_iterator)
print(next(my_iterator))
print(next(my_iterator))

#print(next(my_iterator))

print("#"*50)

for item in iter(mystring):
    print(item)

