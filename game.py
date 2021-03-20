import random
print("Start Game")
c=0
w=0
d=0
# list=["S","W","G"]
print("0-Rock,1-Paper,2-scissor")
while c<3:
    cpu=random.randint(0,2)
    print("Turn",str(c+1))
    you=int(input("Please enter Choice:"))
    while you>2 or you<0:
        print("INVALID")
        you=int(input("Again:"))
        if cpu==you:
            print("Draw")
    elif cpu==0 and you==1:
    print("You Wins")
    elif cpu==1 and you==0:
        print("Computer Wins")
    elif cpu==0 and you==2:
        print("Computer Wins")
    elif cpu==2 and you==0:
        print("You Wins")
    elif cpu==1 and you==2:
        print("You Wins")
    elif cpu==2 and you==1:
        print("Computer Wins")
