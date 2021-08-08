n=int(input("Enter the length"))
l=[0,1]
for i in range(0,n):
    s= l[i] + l[i+1]
    l.append(s)
print(l)