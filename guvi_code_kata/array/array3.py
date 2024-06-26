ns = list(map(int, input().split()))
ans = []

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort(reverse=1)
ans = l1+l2

print(*ans)