a = int(input())

if a <0: print("Error")
if a ==0: print(0)
elif a==1: print(1)
else:
    ans = 1
    for i in range(a-1):
        ans = ans + (i+1)*2+1
    print(ans)