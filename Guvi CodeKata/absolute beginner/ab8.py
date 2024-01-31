[a,b,c] = map(int,input().split())
# X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a
print('{:.2f}'.format(round((((b**2)-(4*a*c))**.5-b)/(2*a),2)))
print('{:.2f}'.format(round((-b-((b**2)-(4*a*c))**.5)/(2*a),2)))