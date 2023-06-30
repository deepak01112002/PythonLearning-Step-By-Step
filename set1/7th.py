#Prime Number

def CheckPrime(number):
  if number <= 1:
    return False

  for i in range(2,int(number**0.5)+1):
     if number%i == 0:
        return False
    
  return True

number = 3
is_prime_num = CheckPrime(number)

if is_prime_num:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
