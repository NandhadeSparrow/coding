[n,m] = list(map(int, input().split()))
sq = n*m
sqrt = sq**.5
if (sqrt % 1) == 0: print('yes')
else: print('no')