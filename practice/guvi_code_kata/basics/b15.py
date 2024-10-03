n = int(input())
x = 0
while True:
    if 2**x > n: 
        print(2**x)
        break
    x += 1