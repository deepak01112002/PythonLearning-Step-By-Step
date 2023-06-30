#selection sort

def SelectionSort(arr):
  n = len(arr)
  for i in range(n):
    min = i
    for j in range(i+1,n):
      if arr[j] < arr[min]:
         min = j
    arr[i],arr[min] = arr[min],arr[i]

list = [64, 25, 12, 22, 11]
SelectionSort(list)
print(list)