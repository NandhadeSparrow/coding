n = input().split()
l = list(map(int, input().split()))

all = []
dup = []
for i in l:
    if i in all: dup.append(i) 
    else: all.append(i)

print(*dup)