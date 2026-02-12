#31/10/2025
#selection sort
import random
arr = []
for e in range(1000):
    arr.append(random.randint(1, 1000))
print(arr)
input("selection sort")

for i in range(len(arr)):
    minpos = i #assume each new pos is the smallest
    for j in range(i+1, len(arr)):
        if arr[j] < arr[minpos]:
            minpos = j #smaller value found (inside loop)
    if minpos != i: #if they dont match (outside loop)
        arr[i],arr[minpos] = arr[minpos],arr[i]
print(arr)