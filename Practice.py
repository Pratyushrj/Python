def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1 :
        return 1
    else :
        a=1
        while(n>1):
            a *= n
            n-=1
        return a
# num=5
# print(f"Factorial of{num} is {factorial(num)}")
def prime(x):
    for i in range(p,q):
        if i>1:
            for j in range(2,i) :
                if (i% j==0):
                    break
            else:
                print(i)
# p=int(input("Enter 1st no"))
# q=int(input("Enter Last no"))
# prime(1)
def primeno(n):
    if n>1:
        for i in range(2,n):
            if (n%i==0):
                print(f"{n} is Not a Prime No")
                break
        else :
            print(f" {n} is Prime No.")
    else:
        print(f"{n} is Not a Prime No")
n=int(input())
primeno(n)