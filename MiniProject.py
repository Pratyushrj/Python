# True
dict = {"Book's Name":[],"location":[]};
dict = {"English":0,"Maths":1,"Science":2,"G.k":3,"M.Sc":4}
print(dict)
while True:
    a=input()
    if a==str("view"):
        print(dict)
    elif a==str("add"):
        c=input("Enter Your Name")
        b=input("Book's Name")
        dict[b]=c
# print(dict)
    elif a==str("return"):
        c = input("Enter Your Name")
        b = input("Book's Name")
        dict2={b : c}
        dict.update(dict2)
    elif a==str("Lend"):
        b = input("Book's Name")
        print(dict)
