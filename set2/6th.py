#concate another way

def ConcatArray(a1,a2):
  newlist=[]
  for x in a1:
    for i in a2:
      newlist.append(x+i)

  return newlist

a1 = ["Hello ", "take "]
a2 = ["Dear", "Sir"]

ans = ConcatArray(a1,a2)
print(ans)