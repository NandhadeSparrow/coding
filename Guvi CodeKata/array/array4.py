n = input().split()
l = list(map(int, input().split()))

count = {}
for i in l:
    count[i] = 0
for i in l:
    count[i] += 1
ans = count.keys()
print(*sorted(ans, key=lambda a: (count[a], a)))