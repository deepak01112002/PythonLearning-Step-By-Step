#add two string

def AddingStr(s1,s2):
  middle = len(s1)//2
  s3 = s1[:middle] + s2 + s1[middle:]
  return s3

s1 = "Ault"
s2 = "Kelly"

ans = AddingStr(s1,s2)
print(ans)