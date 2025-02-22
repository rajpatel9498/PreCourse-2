# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l)
    mergeSort(r)

    i = j = k = 0

    while i<len(l) and j<len(r):
      if l[i] < r[j]:
        arr[k] = l[i]
        i = i + 1
      else:
        arr[k] = r[j]
        j = j + 1
      k = k + 1

    while i < len(l):
      arr[k] = l[i]
      i = i + 1
      k = k + 1

    while j < len(r):
      arr[k] = r[j]
      j = j + 1
      k = k + 1
  
# Code to print the list 
def printList(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
