#27/10/2025

import time
#bubble sort
arr = [17, 2, 29, 8, 5, 22, 11, 1, 30, 9, 4, 19, 12, 25, 3, 13, 28, 21, 10, 24, 18, 14, 7, 6, 20, 26, 15, 23, 16, 27]

print("unsorted:",arr)
time.sleep(1)
print("sorting in:")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

n = len(arr)
for i in range (0,n-1):
    for j in range (0, n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)

print("sorted",arr)