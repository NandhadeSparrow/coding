for i in range(int(input())):
    names = []
    cost = 0
    for j in range(int(input())):
        names.append(input())
    for j in range(len(names)):
        if j>0 and names[j] < names[j-1]:
            for k in range(len(names)):
                if names[k] > names[j]:
                    names.insert(k, names[j])
                    names.pop(j+1)
            cost += 1
                    
                
    print(f"Case #{i+1}: {cost}")