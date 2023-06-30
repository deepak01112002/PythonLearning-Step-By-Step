#Error handling

def ErrorHandle(num,den):
  try:
     result = num / den
     return result
  except ZeroDivisionError:
    return "Cannot Divisible"

num = 5
den = 0

ans = ErrorHandle(num,den)
print(ans)