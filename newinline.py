import time
initial =time.time()
i=0
while(i<=45):
    a=45
    time.sleep(2)
    print(f"No is ",a)
    i=i+1
print("1st program complete",time.time()-initial)
initial1 =time.time()
for i in range(45):
    print("no. is 45")
print("2nd program complete",time.time()-initial)
localtime=time.asctime(time.localtime(time.time()))
print(localtime)