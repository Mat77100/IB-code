import tkinter as tk
import math as m
import time
import threading

def sineWave():
    while True:
        for i in range(1,300):
            Canvas.create_line(i*10,(m.sin(i)*10)+50,(i+1)*10,(m.sin(i+1)*10)+50)
            time.sleep(0.01)

Thread = threading.Thread(target=sineWave,daemon=True)

root = tk.Tk()
root.geometry("1200x980")
Canvas = tk.Canvas(root, height=1100, width=980)
tk.Button(root,command=Thread.start,text="Make sine wave").pack()
Canvas.pack()
Canvas.create_oval(10,10,900,900)

root.mainloop()
