li = list(map(int,input().split()))
ans = li[0]
for i in li:
    if i<ans:ans=i
print(ans)