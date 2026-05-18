#made 18/5/2026
import tkinter as tk
import threading
from time import *

def StartPlayerMoveUp():
    moving = True
    while moving:
        MainCanvas.move(Player, 0, +0.01)
        sleep(0.5) #CANT HAVE SLEEP REMEMBER? IT BLOCKS TKINTER

def StartPlayerMoveUpThread(event):
    MoveThread = threading.Thread(target=StartPlayerMoveUp, daemon=True)
    MoveThread.start()

#def StopPlayerMoveUp():

#def StartPlayerMoveDown():

#def StopPlayerMoveDown():


root = tk.Tk()
root.geometry("1000x600")
MainCanvas = tk.Canvas(root, width=1000, height=600)
MainCanvas.pack()

Player = MainCanvas.create_rectangle(450,250,550,350,fill="Blue")

root.bind('<KeyPress-Up>', StartPlayerMoveUpThread)
#root.bind('<KeyPress-Up>', StopPlayerMoveUpThread)
#root.bind('<KeyRelease-Down>', StartPlayerMoveDownThread)
#root.bind('<KeyRelease-Down>', StopPlayerMoveDownThread)

root.focus_set()
root.mainloop()