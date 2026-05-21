#made 18/5/2026
import tkinter as tk
import threading
from time import *





HorizontalMoveIncrement = 0
VerticalMoveIncrement = 0



def PlayerMovingThread():
    global root
    MainCanvas.move(Player, HorizontalMoveIncrement, VerticalMoveIncrement)
    root.after(30,PlayerMovingThread)
 


def StartPlayerMoveUp(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = -3    
    
def StopPlayerMoveUp(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 0



def StartPlayerMoveDown(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 3

def StopPlayerMoveDown(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 0



def StartPlayerMoveLeft(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = -3

def StopPlayerMoveLeft(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 0



def StartPlayerMoveRight(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 3

def StopPlayerMoveRight(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 0





root = tk.Tk()
root.geometry("1000x600")
MainCanvas = tk.Canvas(root, width=1000, height=600)
MainCanvas.pack()

Player = MainCanvas.create_rectangle(450,250,550,350,fill="Blue")



root.bind('<KeyPress-Up>', StartPlayerMoveUp)
root.bind('<KeyRelease-Up>', StopPlayerMoveUp)
root.bind('<KeyPress-Down>', StartPlayerMoveDown)
root.bind('<KeyRelease-Down>', StopPlayerMoveDown)
root.bind('<KeyPress-Left>', StartPlayerMoveLeft)
root.bind('<KeyRelease-Left>', StopPlayerMoveLeft)
root.bind('<KeyPress-Right>', StartPlayerMoveRight)
root.bind('<KeyRelease-Right>', StopPlayerMoveRight)

PlayerMovingThread()

#MoveThread = threading.Thread(target=PlayerMovingThread, daemon=True)
#MoveThread.start()

root.focus_set()
root.mainloop()