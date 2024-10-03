a = int(input())
if a == 0:
    print("NULL")
else:
    ans = []
    for i in range(a):
        ans.append(9*(i+1))
    print(*ans, sep=" ")