from random import randint

InitialChoice = 0
switchConfirm = 0
switchRandom = 0
n = 100000

for i in range(n):
    doors = []
    putcar = randint(0,2)
    for i in range(3):
        if i == putcar: doors.append('c')
        else: doors.append('g')
    ch1 = randint(0,2)
    doors2 = []
    if doors[ch1] == 'c': 
        doors2 = ['c', 'g']
        InitialChoice += 1
    else: 
        doors2 = ['g', 'c']
    switch = randint(0,1)
    if doors2[switch] == 'c': switchRandom += 1
    switch = 1
    if doors2[switch] == 'c': switchConfirm += 1


print("Winning probablity for initial choice: ",round(InitialChoice/n*100), "%")
print("Winning probablity if switching is random: ",round(switchRandom/n*100), "%")
print("Winning probablity if switching is confirmed: ",round(switchConfirm/n*100), "%")