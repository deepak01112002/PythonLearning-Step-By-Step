#FACTORIAL

def Factorial(number):
  if number<0:
    return None
  elif number == 0:
    return 1
  else:
    result = 1
    for i in range(1,number+1):
      result *= i

    return result

Value = Factorial(5)
print(Value)