marks=int(input("Enter your mark:"))

def findpassorfail(marks):
    if(marks<0 or marks>100):
        print("Invalid marks")
    elif(marks<35):
        print("Fail")
    else:
        print("Pass")

findpassorfail(marks)
