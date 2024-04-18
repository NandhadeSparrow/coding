n = int(input())

l = list(map(int,input().split()))

small = 0
large = 0

for i in range(n):
    if l[i] < l[small]:
        small = i
    if l[i]  > l[large]:
        large = i
print(large-small)