#made 18/5/2026
import tkinter as tk
from time import *
import math
import random

'''

IDEA FOR HOW TO MAKE THIS A GAME, THINK CITYBUILDER/IDLE/TYCOON GAME, EACH SQUARE OF PAINT WILL DO SMTH (DEPENDING ON THE COLOUR)
also make cube^TM smaller
or idk like u can paint to fight



'''

HorizontalMoveIncrement = 0
VerticalMoveIncrement = 0


#MAKE THIS A CLASS
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
    VerticalMoveIncrement = -4  
    
def StopPlayerMoveUp(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 0



def StartPlayerMoveDown(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 4

def StopPlayerMoveDown(event):
    global VerticalMoveIncrement
    VerticalMoveIncrement = 0



def StartPlayerMoveLeft(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = -4

def StopPlayerMoveLeft(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 0



def StartPlayerMoveRight(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 4

def StopPlayerMoveRight(event):
    global HorizontalMoveIncrement
    HorizontalMoveIncrement = 0





#ENEMY
class Enemy():
    def __init__(self,speed,size,colour,MainCanvas, SpawnX, SpawnY):
        self.MainCanvas = MainCanvas
        self.speed = speed
        self.colour = colour
        self.size = size
        self.ID = self.MainCanvas.create_rectangle(SpawnX,SpawnY,SpawnX+self.size,SpawnY+self.size,fill=str(self.colour))

        self.MoveToPlayer()

    def MoveToPlayer(self):
        EnemyX1 = self.MainCanvas.coords(self.ID)[0]
        EnemyY1 = self.MainCanvas.coords(self.ID)[1]
        EnemyX2 = self.MainCanvas.coords(self.ID)[2]
        EnemyY2 = self.MainCanvas.coords(self.ID)[3]
        #center of enemy:
        EnemyCoord = [(EnemyX1 + EnemyX2)/2 , (EnemyY1 + EnemyY2)/2]

        PlayerX1 = self.MainCanvas.coords(Player)[0]
        PlayerY1 = self.MainCanvas.coords(Player)[1]
        PlayerX2 = self.MainCanvas.coords(Player)[2]
        PlayerY2 = self.MainCanvas.coords(Player)[3]
        #center of player:
        PlayerCoord = [(PlayerX1 + PlayerX2)/2 , (PlayerY1 + PlayerY2)/2]

        Xcomponent = EnemyCoord[0] - PlayerCoord[0]
        Ycomponent = EnemyCoord[1] - PlayerCoord[1]

        TrueDistance = math.sqrt(Xcomponent**2 + Ycomponent**2)

        NormalX = Xcomponent / TrueDistance
        NormalY = Ycomponent / TrueDistance

        SpeedX = self.speed * NormalX
        SpeedY = self.speed * NormalY

        self.MainCanvas.move(self.ID, SpeedX*-1, SpeedY*-1)
        self.MainCanvas.after(100, self.MoveToPlayer)


'''IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MAKE THE GAME RUN ON ONE CENTRAL LOOP
basically instead of several .after, have one .after running a functiuon called update or smth that then contains command to do stuff, for example you can remove the .after in the enemy MoveToPlayer method by simply calling MoveToPlayer in the central update loop
'''



'''
ENEMY MOVEMENT:
take coordinates of enemy and player
find the difference between them to give the x and y components
use pythagoras to find the true distance
Normalize by dividing each component by the true distance
multiply the normalized x and y by the max speed
move the enemy, repeat per frame
'''






#Mouse stuff

class brush():
    def __init__(self, MainCanvas):
        self.MainCanvas = MainCanvas
        self.MouseX = 0
        self.MouseY = 0
        self.IsPressed = False
        self.SquareSize = 5

        MainCanvas.bind('<Motion>',self.MousePositionTracker)
        MainCanvas.bind('<Button-1>', self.MouseClick)
        MainCanvas.bind('<ButtonRelease-1>', self.MouseRelease)
        MainCanvas.bind('<MouseWheel>',self.ScrollWheel)

        self.SquareList = []

        self.BrushUpdate()
       

    def MousePositionTracker(self, event):
        self.MouseX, self.MouseY = event.x, event.y
        
    def MouseClick(self,event):
        self.IsPressed = True
    def MouseRelease(self,event):
        self.IsPressed = False
    
    def ScrollWheel(self,event):
        if event.delta > 0:
            self.SquareSize +=1
        elif self.SquareSize !=1:
            self.SquareSize -=1

    def BrushUpdate(self):
        Name = 0
        if self.IsPressed == True:
            S = self.SquareSize
            SquareID = self.MainCanvas.create_rectangle(
                self.MouseX + S,
                self.MouseY + S,
                self.MouseX - S,
                self.MouseY - S,
                fill="red")
            self.SquareList.append(SquareID)
            self.Delay(SquareID)
        self.MainCanvas.after(20,self.BrushUpdate)

    def Delay(self, SquareID):
        self.MainCanvas.after(1500, lambda: self.RemoveSquare(SquareID),)

    def RemoveSquare(self, SquareID):

        self.SquareList.remove(SquareID)  
        self.MainCanvas.delete(SquareID)

    def RemoveSquares(self):
        if len(self.SquareList) > 0:
            Square_To_Delete = self.SquareList.pop(0)
            self.MainCanvas.delete(Square_To_Delete)
        self.MainCanvas.after(1000,self.RemoveSquares)

def SpawnStandardEnemy():
    Enemy(5,15,"red",MainCanvas, random.randint(0,1000), random.randint(0,600))

def SpawnRandomEnemy():
    colours = ["red","blue","green","yellow","black","yellow","cyan","orange"]
    Enemy(random.randint(1,10),random.randint(10,25),random.choice(colours),MainCanvas, random.randint(0,1000), random.randint(0,600))






#Tkinter

root = tk.Tk()
root.geometry("1000x700")
MainCanvas = tk.Canvas(root, width=1000, height=600)
MainCanvas.pack()

SpawnEnemyButton = tk.Button(root,text="Spawn standard enemy", command=SpawnStandardEnemy)
SpawnRandomEnemyButton = tk.Button(root,text="Spawn random enemy", command=SpawnRandomEnemy)

SpawnRandomEnemyButton.pack()
SpawnEnemyButton.pack()
Player = MainCanvas.create_rectangle(450,250,500,300,fill="Blue")
line = False

MainBrush = brush(MainCanvas)



#Bindings
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


PlayerMovingThread()

#MoveThread = threading.Thread(target=PlayerMovingThread, daemon=True)
#MoveThread.start()

root.focus_set()
root.mainloop()