# def fib(n):
#     if n<0 :
#         print("Error input")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else :
#         return fib(n-1)+fib(n-2)
# print(fib(9))
# print(ord("a"))
# print(pow(3,2))
def searcher():
    import time
    book = "This is a Book"
    time.sleep(3)
    while True :
        text =(yield)
        if text in book:
            print("Your text is present")
        else :
            print("Your text is NOT present")
search = searcher()
print("Started.......")
next(search)
print("Next method run . . .")
search.send("Books")