sets = int(input())
matched = False
for a in range(sets):
    s1 = input()
    s2 = input()
    match = ""
    for i in range(len(s2)):
        for j in range(len(s2)-i):
            match = s2[0:i]+s2[i+j+1:]
            if match==s1:
                print("Case #{}: {}".format(a+1, len(s2)-len(match))
                matched = True
                break
        if matched:
            break
    if not matched:
        print("Case #{}: IMPOSSIBLE".format(a+1))
    matched = False