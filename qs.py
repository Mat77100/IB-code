#30/10/2025
import random
import time

def quicksort(Data):    
    if len(Data) <=1:
        return Data
    
    pivot = Data[0]
    rest = Data[1:]
    
    
    
    LessOrEqual = []
    Larger = []
    
    for x in rest:
        if x <= pivot:
            LessOrEqual.append(x)
        else:
            Larger.append(x)
    
    sortedSmaller = quicksort(LessOrEqual)
    sortedLarger = quicksort(Larger)
    return sortedSmaller + [pivot] + sortedLarger
    

Data = []
for i in range(10000):
    Data.append(random.randint(1,1000))
print(Data)

input("quicksort")
s = time.time()
Data1 = quicksort(Data)
e = time.time()
t = e-s
print(Data1)
print(t)

input("bubblesort")
s = time.time()
n = len(Data)
for i in range (0,n-1):
    for j in range (0, n-1-i):
        if Data[j] > Data[j+1]:
            Data[j], Data[j+1] = Data[j+1], Data[j]
e = time.time()
print(Data)
print(e-s)