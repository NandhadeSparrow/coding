a= int(input())

x= []
y= []
for i in str(a):
    if int(i)%2 ==0: x.append(i)
    else: y.append(int(i))
x.sort()
y.sort()
print(*x)
print(*y)