class Emp:
    pass

    def __init__(self,aname,asal,arole):
        self.name=aname
        self.sal=asal
        self.role=arole

    def printdetails (self):
        return f"Name is ",self.name,"Salary is ",self.sal
# harry=Emp()
harry=Emp("HArrY",3333,"Inst")
# larry=Emp()
# harry.name="HARRY"
# harry.sal=300
print(harry.printdetails())
print(harry.name)