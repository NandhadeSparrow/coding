from random import randint
n = 100000
ans=0
for i in range(n):
    if randint(1,10)>6: ans +=1

print(round(ans/n*100), "%")
