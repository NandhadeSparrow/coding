from random import randint

prob = 0
n = 10000000

for i in range(n):
    if randint(1,3) != 1: prob+=1

print("Winning Probablity by Switching: ",round(prob/n*100), "%")