#made 18/5/2026
import tkinter as tk
from time import *





HorizontalMoveIncrement = 0
VerticalMoveIncrement = 0



def PlayerMovingThread():
    global root,HorizontalMoveIncrement,VerticalMoveIncrement

    if (MainCanvas.coords(Player))[1] < 0:
        DistanceToEdge = (MainCanvas.coords(Player))[1]
        VerticalMoveIncrement = 0
        MainCanvas.move(Player,0,DistanceToEdge*-1)
    if (MainCanvas.coords(Player))[3] > 600:
        DistanceToEdge = 600 - (MainCanvas.coords(Player))[3]
        VerticalMoveIncrement = 0
        MainCanvas.move(Player,0,DistanceToEdge)
    if (MainCanvas.coords(Player))[0] < 0:
        DistanceToEdge = (MainCanvas.coords(Player))[0]
        HorizontalMoveIncrement = 0
        MainCanvas.move(Player,DistanceToEdge*-1,0)
    if (MainCanvas.coords(Player))[2] > 1000:
        DistanceToEdge = 1000 - (MainCanvas.coords(Player))[2]
        HorizontalMoveIncrement = 0
        MainCanvas.move(Player,DistanceToEdge,0)
    
    MainCanvas.move(Player, HorizontalMoveIncrement, VerticalMoveIncrement)
    root.after(25,PlayerMovingThread)
 


def StartPlayerMoveUp(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = -2   
    
def StopPlayerMoveUp(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 0



def StartPlayerMoveDown(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 2

def StopPlayerMoveDown(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 0



def StartPlayerMoveLeft(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = -2

def StopPlayerMoveLeft(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 0



def StartPlayerMoveRight(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 2

def StopPlayerMoveRight(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 0


def PlayerShoot(event):
    global line
    if line != False:
        MainCanvas.delete(line)
        line = False
        return
    else:
        PlayerX = (MainCanvas.coords(Player)[0] + MainCanvas.coords(Player)[2])/2 #Decimal pixels possible??
        PlayerY = (MainCanvas.coords(Player)[1] + MainCanvas.coords(Player)[3])/2 #Decimal pixels possible??
        line = MainCanvas.create_line(PlayerX,PlayerY,PlayerX+1000,PlayerY, )
        root.after(PlayerShoot,1000)




root = tk.Tk()
root.geometry("1000x600")
MainCanvas = tk.Canvas(root, width=1000, height=600)
MainCanvas.pack()

Player = MainCanvas.create_rectangle(450,250,550,350,fill="Blue")
line = False


root.bind('<KeyPress-Up>', StartPlayerMoveUp)
root.bind('<KeyRelease-Up>', StopPlayerMoveUp)
root.bind('<KeyPress-Down>', StartPlayerMoveDown)
root.bind('<KeyRelease-Down>', StopPlayerMoveDown)
root.bind('<KeyPress-Left>', StartPlayerMoveLeft)
root.bind('<KeyRelease-Left>', StopPlayerMoveLeft)
root.bind('<KeyPress-Right>', StartPlayerMoveRight)
root.bind('<KeyRelease-Right>', StopPlayerMoveRight)

root.bind('<KeyPress-w>', StartPlayerMoveUp)
root.bind('<KeyRelease-w>', StopPlayerMoveUp)
root.bind('<KeyPress-s>', StartPlayerMoveDown)
root.bind('<KeyRelease-s>', StopPlayerMoveDown)
root.bind('<KeyPress-a>', StartPlayerMoveLeft)
root.bind('<KeyRelease-a>', StopPlayerMoveLeft)
root.bind('<KeyPress-d>', StartPlayerMoveRight)
root.bind('<KeyRelease-d>', StopPlayerMoveRight)

root.bind('<KeyPress-space>',PlayerShoot)

PlayerMovingThread()

#MoveThread = threading.Thread(target=PlayerMovingThread, daemon=True)
#MoveThread.start()

root.focus_set()
root.mainloop()