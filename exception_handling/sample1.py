while True:
    try:
        raise Exception
        x = int(input("Please enter a number: "))
        break
    #except ValueError as err:
    #    print(err)
    #    print("Oops!  That was no valid number.  Try again...")
    except ImportError as err:
        print("I am here")
        print(err)
        break
    except Exception as err:
        print("I caught this")
        print(err)
        break
    except BaseException as err:
        print(err)
        break

#except (RuntimeError, TypeError, NameError):
#pass