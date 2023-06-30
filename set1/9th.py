#Fibanacho sequence

def Fibbonaci(n):
    sequence = []
    if n <= 0:
        return sequence

    if n >= 1:
        sequence.append(0)

    if n >= 2:
        sequence.append(1)

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence

value = Fibbonaci(5)
print(value)

value = [x**2 for x in range(1,11)]
print(value)