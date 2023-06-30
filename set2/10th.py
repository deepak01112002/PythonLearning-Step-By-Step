#tuplemodify

tuple1 = (11, [22, 33], 44, 55)
arr = list(tuple1)
arr[1][0] = 222
typle1 = tuple(arr)
print(typle1)