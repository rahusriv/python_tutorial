while True:
    try:
        raise ImportError
        x = int(input("Please enter a number: "))
        break
    #except ValueError as err:
    #    print(err)
    #    print("Oops!  That was no valid number.  Try again...")
    except ImportError as err:
        print(err)
    except Exception as err:
        print("I caught this")
        print(err)
    except BaseException as err:
        print(err)

#except (RuntimeError, TypeError, NameError):
#pass