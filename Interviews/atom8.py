dict = {a:a for a in "abcdefghijklmnopqrstuvwxyz"}

def change():
  ok = True

  for i in dict.keys():
    if dict[dict[i]] < dict[i]:
      dict[i] = dict[dict[i]]
      ok = False
    if not ok:
      change()
  
def ans(s1, s2, s3):
  out = ""

  for c1, c2 in zip(s1, s2):
    if dict[c1] < dict[c2]:
      dict[c2] = dict[c1]
    else:
      dict[c1] = dict[c2]
    
    change()
      
  for c in s3:
    out += dict[c]
      
  print(out)


ans(input(), input(), input())