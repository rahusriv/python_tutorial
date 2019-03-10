marks = int(input("Enter you marks :"))

if ( (marks>=0) and (marks<40) ):
    print("F")
elif( (marks>=40) and (marks<60) ):
    print("D")
elif( (marks>=60) and (marks<80) ):
    print("C")
elif( (marks>=80) and (marks<90) ):
    print("B")
elif( (marks>=90) and (marks<=100) ):
    print("A")
else:
    print("Incorrect value .Marks should ne withon 0-100")