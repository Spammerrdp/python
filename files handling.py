#method 1
f1 = open("your txt file path","r")
print(f1.read())
f1.close()
#method 2
with open("your txt file path","r") as f1:
    print(f1.read())