#Conditional Printing

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
  if i > 500:
    break
  if i % 5==0:
    if i > 150 :
      continue
    print(i)  