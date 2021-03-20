print("Enter 1st no")
a=int(input())
print("Enter 2nd no")
b=int(input())
print("Enter operation :+,-,*,/")
c=input()
if(a==9 and b==8 and c==str("*")):
    print("54")
elif(a==5 and b==7 and c==str("+")):
    print("13")
else:
    if(c==str("+")):
        d=a+b
        print(d)
    elif (c == str("-")):
        d = a - b
        print(d)
    elif (c == str("*")):
        d = a * b
        print(d)
    elif (c == str("/")):
        d = a / b
        print(d)
    else:
        print("Error")