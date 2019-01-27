def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    #except ValueError:
    #    print("Wrong type of value given")
    except BaseException:
        print("Unown exception")
    else:
        print("result is", result)
    finally:
        raise Exception
        print("executing finally clause")

divide(2, 1)
print("*"*50)
divide(2, 0)
print("*"*50)
divide("2", "1")