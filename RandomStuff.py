import random as rng
import tkinter as tk
import time

global A
A = []
for i in range(1,101):
    A.append(i)


#randomiser
def randomiser(A):
    for i in range(0,len(A)-1):
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


def randFun():
    global A
    global lineList
    global Canvas
    A = randomiser(A)
    def updatelines(i=0):
            if  i < len(lineList):
                x1,y1,x2,y2 = Canvas.coords(lineList[i])
                Canvas.coords(lineList[i],x1,y1,x2,A[i]*5)  
                main.after(5,updatelines,i+1)
    updatelines()
    

        

def QuickSortStart():
    global A
    A = QuickSort(A)



main = tk.Tk()
main.geometry("1250x700")
tk.Button(main,text="QUIT",command=main.destroy).pack()
Canvas = tk.Canvas(main,width=1250,height=600)
tk.Button(main,text="Randomise!",command=randFun).pack()
tk.Button(main,text="Sort!",command=QuickSortStart).pack()
Canvas.pack()
distance = 19
lineList = []
for i in range(0,100):
    line = Canvas.create_line(i+distance,500,i+distance,A[i]*5,fill="blue",width=10)
    lineList.append(line)
    distance += 10
main.mainloop()