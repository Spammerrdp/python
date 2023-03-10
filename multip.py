a = int(input("enter number"))
b = int(input("enter number"))
l1 = []
def callme(n):
    for i in range(1,a+1):
        l1.append(i)
    n -=1
    if n !=0:
        callme(n)
    else:
        print(f"{a} x {b} = {len(l1)}")
callme(b)
