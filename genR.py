# def getNum (x):
#     for i in range(x):
#         yield i
#
# seq = getNum (2)
# print(seq.__next__())
# print(seq.__next__())



# l=[]
# for i in range(100) :
#     if i%3==0 :
#         l.append(i)
# print(l)

# l=[i for i in range(100) if i%3==0]
# print(l)

# dict={ i:f"item{i}" for i in range(1,11)}
# print(dict)
# dict1={v:k for k,v in dict.items()}
# print(dict1)

i=int(input())
a=[]
for item in range (i) :
    b=input()
    a.append(b)
print(a)