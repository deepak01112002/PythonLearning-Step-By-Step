#Concatinate  the array index

def Concat(a1,a2):
  newlist=[]
  length = min(len(a1),len(a2))
  for i in range(length):
    newlist.append(a1[i]+a2[i])
  if(len(a1)>length):
    newlist.extend(a1[length:])
  elif(len(a2)>length):
    newlist.extend(a2[length:])
  return newlist

a1 = ["M", "na", "i", "Ke"]
a2 = ["y", "me", "s", "lly"]

ans = Concat(a1,a2)
print(ans)

