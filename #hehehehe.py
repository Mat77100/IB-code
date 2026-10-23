#hehehehe
import tkinter as tk
Main = tk.Tk()
Main.geometry("600x600")

CheekyButton = tk.Button(Main,text="Click me!",width=15,height=2)
CheekyButton.place(x=250,y=250)

MouseClose = False

def CheckMouseHover(event):
        M_x = event.x
        M_y = event.y
        #print(M_x,M_y)
        B_x = CheekyButton.winfo_rootx() + 7
        B_y = CheekyButton.winfo_rooty() + 1
        #print(B_x,B_y)
        DistanceX = B_x - M_x
        DistanceY = B_y - M_y
        print(DistanceX,DistanceY)

        if DistanceX < 180 and DistanceY < 180:
                CheekyButton.place(x=B_x-1,y=B_y-1)
        if DistanceX < -180 and DistanceY < -180:
                        CheekyButton.place(x=B_x+1,y=B_y+1)

Main.bind("<Motion>",CheckMouseHover)

Main.mainloop()
