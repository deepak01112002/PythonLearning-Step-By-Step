#print answer 

def PrintList(a1,a2):
  a2.reverse()
  for x,i in zip(a1,a2):
    print(x,i)

a1 = [10, 20, 30, 40]
a2 = [100, 200, 300, 400,500]

answer = PrintList(a1,a2)
print(answer)