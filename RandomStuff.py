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

def BubbleStep():
    global A,i,j
    if j < (len(A)-1):
        if i <(len(A)-j-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                updatelines()
            i += 1
            main.after(10,BubbleStep)
        else:
            i = 0
            j += 1
            main.after(10,BubbleStep)
    else:
        randbtn.config(state="normal")
        sortbtn.config(state="normal")
              
            


def randFun():
    randbtn.config(state="disabled")
    sortbtn.config(state="disabled")
    global A,lineList,Canvas,unlock
    unlock = True
    A = randomiser(A)
    updatelines()


def updatelines(i=0):
  global unlock
  if  i < len(lineList):
      x1,y1,x2,y2 = Canvas.coords(lineList[i])
      Canvas.coords(lineList[i],x1,y1,x2,A[i]*5)  
      main.after(10,updatelines,i+1)
  else:
      if unlock:
          randbtn.config(state="normal")
          sortbtn.config(state="normal")
          unlock = False

def StartSort():
    randbtn.config(state="disabled")
    sortbtn.config(state="disabled")
    global i, j
    i = 0
    j = 0
    BubbleStep()



main = tk.Tk()
main.geometry("1250x700")
tk.Button(main,text="QUIT",command=main.destroy).pack()
Canvas = tk.Canvas(main,width=1250,height=600)
randbtn = tk.Button(main,text="Randomise!",command=randFun)
sortbtn = tk.Button(main,text="Sort!",command=StartSort)
randbtn.pack()
sortbtn.pack()
Canvas.pack()
distance = 19
lineList = []
for i in range(0,100):
    line = Canvas.create_line(i+distance,500,i+distance,A[i]*5,fill="blue",width=10)
    lineList.append(line)
    distance += 10
main.mainloop()
