[l, r] = list(map(int, input().split()))
primes = []
for i in range(l, r+1):
    prime = True
    for j in range(2, i+1):
        if i == j: continue
        if  i % j == 0: 
            prime = False
            break
    if prime:
        primes.append(i)
print(len(primes))