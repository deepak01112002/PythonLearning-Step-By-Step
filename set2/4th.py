#Sorting

def ArrangeStr(s1):
  lower = ""
  upper = ""
  for x in s1:
    if x.islower():
      lower += x
    else:
      upper += x
  ans = lower + upper
  return ans

s1 = "PyNaTive"
answer = ArrangeStr(s1)
print(answer)