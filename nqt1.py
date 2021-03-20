print("Enter the Oxygen in 1St round")
a1=int(input())
b1=int(input())
c1=int(input())
print("Enter the Oxygen in 2nd round")
a2=int(input())
b2=int(input())
c2=int(input())
print("Enter the Oxygen in 3rd round")
a3=int(input())
b3=int(input())
c3=int(input())
a=(a1+a2+a3)/3
b=(b1+b2+b3)/3
c=(c1+c2+c3)/3
if a>=70 :
    print("1st Selected     :   Oxygen level is",a)
else:
    print("1st Not Selected     :   Oxygen level is",a)
if b>=70 :
    print("2nd Selected     :   Oxygen level is",b)
else:
    print("2nd Not Selected     :   Oxygen level is",b)
if c>=70 :
    print("3rd Selected     :   Oxygen level is",c)
else:
    print("3rd Not Selected     :   Oxygen level is",c)
