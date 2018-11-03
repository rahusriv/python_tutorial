
count = 0

def counterFunction1():
    global count
    print("1. I got called")
    count = count+1
    print(count)

def counterFunction2():
    global count
    print("2. I got called")
    count = count +1
    print(count)

def counterFunction3():
    global count
    print("3. I got called")
    count = count +1
    print(count)

print("Before call count = {}".format(count))
counterFunction1()
counterFunction1()
counterFunction1()
counterFunction1()
counterFunction1()

counterFunction2()
counterFunction2()
counterFunction2()

counterFunction3()
counterFunction3()

print("After call count = {}".format(count))



