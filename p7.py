l = [["science",77],["maths",90],["python",90]]
t = 0
n = 0
for i in l:
    t += int(i[1])
    n+=100
print(f"total marks:{t}\npercentage:{(t/n)*100}")