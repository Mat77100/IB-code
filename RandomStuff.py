import random as rng
import tkinter as tk
import time
import threading
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

def SelectionSort():
    global sorted,A,speed
    if sorted:
        SSortThread.join()
        randbtn.config(state="normal")
        sortbtn.config(state="normal")
        return
    for i in range(len(A)):
        minpos = i #assume each new pos is the smallest
        for j in range(i+1, len(A)):
            if A[j] < A[minpos]:
                minpos = j #smaller value found (inside loop)
        if minpos != i: #if they dont match (outside loop)
            A[i],A[minpos] = A[minpos],A[i]
        time.sleep(speed/1000)
    sorted = True
    SSortThread.join()
    randbtn.config(state="normal")
    sortbtn.config(state="normal")
    return
    
    


def BubbleStep():
    global A,i,j,sorted,speed
    if j < (len(A)-1) and not sorted:
        if i <(len(A)-j-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                updatelines()
            i += 1
            main.after(speed,BubbleStep)
        else:
            i = 0
            j += 1
            main.after(speed,BubbleStep)
    else:
        randbtn.config(state="normal")
        sortbtn.config(state="normal")
        sorted = True




def randFun():
    randbtn.config(state="disabled")
    sortbtn.config(state="disabled")
    global A,lineList,Canvas,unlock
    unlock = True
    A = randomiser(A)
    updatelines()


def updatelines(i=0):
  global unlock,sorted,speed
  if  i < len(lineList):
      x1,y1,x2,y2 = Canvas.coords(lineList[i])
      Canvas.coords(lineList[i],x1,y1,x2,A[i]*5)  
      main.after(speed,updatelines,i+1)
  else:
      if unlock:
          randbtn.config(state="normal")
          sortbtn.config(state="normal")
          unlock = False
          sorted = False

def StartSort():
    randbtn.config(state="disabled")
    sortbtn.config(state="disabled")
    global i, j,min_idx
    i = 0
    j = 0
    min_idx = 0
    SSortThread.start()
    updatelinesThread.start()

def UpdateLineslive():
    global sorted,lineList,speed
    while not sorted:
        for i in range(len(lineList)):
            x1,y1,x2,y2 = Canvas.coords(lineList[i])
            Canvas.coords(lineList[i],x1,y1,x2,A[i]*5)  
            time.sleep(0.0001)
    UpdateLineslive.join()
    

sorted = True
def SlowSpeed():
    global speed
    speed = 30
    slowbtn.config(bg="grey")
    mediumbtn.config(bg="white")
    fastbtn.config(bg="white")
    zoombtn.config(bg="white")
def MediumSpeed():
    global speed
    speed = 10
    slowbtn.config(bg="white")
    mediumbtn.config(bg="grey")
    fastbtn.config(bg="white")
    zoombtn.config(bg="white")
def FastSpeed():
    global speed
    speed = 5
    slowbtn.config(bg="white")
    mediumbtn.config(bg="white")
    fastbtn.config(bg="grey")
    zoombtn.config(bg="white")
def ZoomSpeed():
    global speed
    speed = 1
    slowbtn.config(bg="white")
    mediumbtn.config(bg="white")
    fastbtn.config(bg="white")
    zoombtn.config(bg="grey")

speed = 10

SSortThread = threading.Thread(target=SelectionSort)
updatelinesThread = threading.Thread(target=UpdateLineslive,daemon=True)
main = tk.Tk()
main.geometry("1500x700")
tk.Button(main,text="QUIT",command=main.destroy).pack()
Canvas = tk.Canvas(main,width=1250,height=600)
randbtn = tk.Button(main,text="Randomise!",command=randFun)
sortbtn = tk.Button(main,text="Sort!",command=StartSort)
slowbtn = tk.Button(main,text="Slow",command=SlowSpeed,anchor="e",)
mediumbtn = tk.Button(main,text="Medium",command=MediumSpeed,anchor="e",bg="grey")
fastbtn = tk.Button(main,text="Fast",command=FastSpeed,anchor="e")
zoombtn = tk.Button(main,text="ZOOM!",command=ZoomSpeed,anchor="e")
slowbtn.pack(side="right")
mediumbtn.pack(side="right")
fastbtn.pack(side="right")
zoombtn.pack(side="right")
tk.Label(main,text="Speed:",anchor="e").pack(side="right")
randbtn.pack()
sortbtn.pack()
Canvas.pack()
distance = 19
lineList = []
for i in range(0,100):
    line = Canvas.create_line(i+distance,501,i+distance,A[i]*5,fill="blue",width=10)
    lineList.append(line)
    distance += 10
main.mainloop()
