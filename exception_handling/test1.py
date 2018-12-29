
while(True):

    try :
        num = int(input("Enter a number :"))
        res = 100/num
        print("Result is : {}".format(res))
        break
    except ZeroDivisionError:
        print("You divided by zero")
    except ValueError:
        print("Not an integer")
    except BaseException:
        print("Some error")
