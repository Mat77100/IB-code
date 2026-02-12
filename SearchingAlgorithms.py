#linear search
arr = []
for i in range(1,101):
    arr.append(i)
print(arr)
target = int(input("insert target:" ))

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

result = linear_search(arr,target)
if result != -1:
    print("found in index", result)
else:
    print("element not found")


#recursive linear search

def rec_lin_search(arr, target, index):
    if index == len(arr):
        return -1 #not found
    if arr[index] == target:
        return index
    return rec_lin_search(arr, target, index + 1)

print(rec_lin_search(arr,target,0))

while True:
    move_to_rec_s = input("move to recursive search? (y/n) ")
    if move_to_rec_s == "y":
        break
    
#binary search
target = int(input("insert target:" ))

def rec_s(arr, target):
    left = 0
    right = len(arr)-1
    mid = (left+right)//2    
    
    while left<= right:
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid +1
        if target < arr[mid]:
            right = mid-1
        mid = (left+right)//2
    return -1

print(rec_s(arr, target))