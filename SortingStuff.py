#sortin n' stuff
import random as rng
import tkinter as tk


#randomiser
def randomiser(A):
    for i in range(len(A)):
        r1 = rng.randint(0,len(A)-1)
        r2 = rng.randint(0,len(A)-1)
        A[r1], A[r2] = A[r2], A[r1]
    return A


def makeRandomisedArr(Scale):
    A = []
    for i in range (1,Scale+1):
        A.append(i)
    A = randomiser(A)
    return A


#quick sort
def QuickSort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    rest = A[1:]

    larger = []
    smaller = []

    for i in range (len(rest)):
        if rest[i] >= pivot:
            larger.append(rest[i])
        else:
            smaller.append(rest[i])
    #print(rest)
    #print(smaller)
    #print(larger)
    sorted_smaller = QuickSort(smaller)
    sorted_larger = QuickSort(larger)
    return sorted_smaller + [pivot] + sorted_larger

#print("sorted array: ",QuickSort(A))

#selection sort
def SelectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        if min_idx!=i:
            A[i], A[min_idx] = A[min_idx],A[i]
    return A

def BubbleSort(A):
    for j in range(len(A)-1):
        for i in range(len(A)-j-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
    return A

def printQS():
    print(QuickSort(A))
    randomiser(A)
def printSS():
    print(SelectionSort(A))
    randomiser(A)
def printBS():
    print(BubbleSort(A))
    randomiser(A)
def printArr():
    print(A)

def nextwin():
    global A
    A = makeRandomisedArr(S.get())
    rootWin.withdraw()
    
    win = tk.Toplevel(rootWin)

    l2 = tk.Label(win,text = "Pick a sorting algorythm:")
    pb = tk.Button(win, text = "Print randomised array", width = 20, command = printArr)
    b1 = tk.Button(win, text = "Quick Sort", width = 30, command=printQS)
    b2 = tk.Button(win, text = "Selection Sort", width =30, command=printSS)
    b3 = tk.Button(win, text = "Bubble Sort", width = 30, command=printBS)

    pb.pack()
    l2.pack()
    b1.pack()
    b2.pack()
    b3.pack()

rootWin = tk.Tk()

S = tk.Scale(rootWin, from_=10, to=10000, orient="horizontal",resolution=10, length = 300, width = 20)
l1 = tk.Label(rootWin, text = "Amount of element in the unsorted array:")
NB = tk.Button(rootWin, text = "Next", width = 10, command=nextwin)
S.pack()
l1.pack()
NB.pack()

rootWin.mainloop()



'''
print("please select a soring method:")
print("1 -- Quick Sort")
print("2 -- Selection Sort")
print("3 -- Bubble Sort")
while True:
    try:
        action = int(input("input: "))
        break
    except:
        print("Invalid input")

if action == 1:
    print(QuickSort(A))
elif action == 2:
    print(SelectionSort(A))
elif action == 3:
    print(BubbleSort(A))

print(A)

'''