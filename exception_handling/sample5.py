#Raising an exception

#raise NameError('HiThere')

#raise ValueError

try:
    raise NameError()
    #raise NameError("Manually raised this error")
except NameError as err:
    print("An excepton flew by !")
    print(err)
