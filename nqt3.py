# a=int(input(""))
# b=int(input(""))
# c=int(input(""))
# d= 5*b*c
# if d>=a :
#     print("1")
# elif d<a :
#     print("0")
# else :
#     print("INVALID INPUT")
# =================================================
x=int(input("No. of amount"))
a=[]
b=0
if x>=5 :
    c=x//5
    x=x-c*5
    # b=b+1
    a.append(5)
if x>=3 :
    c=x//3
    x=x-c*3
    # b=b+1
    a.append(3)
if x>=2 :
    x=x%2
    print(a)
    # b=b+1
    a.append(2)
if x>=1 :
    x=x%1
    print(a)
    # b=b+1
    a.append(1)
d=len(a)
print(d)