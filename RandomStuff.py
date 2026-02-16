import random
import tkinter as tk

A = []
for i in range(0,10000):
    A.append(random.randint(1,100))
print(A)

results = [0]*100
print (results)
for j in range(0,100):
    total = 0
    for i in range(0,len(A)):
        if A[i] == j:
            total +=1
    results[j] = total
print("")
results[0] = "amount of numbers equivelent to the index:"
print("Amount of each number genarated by random (1 to 100):")
print(results)

main = tk.Tk()
tk.Button(main,text="QUIT",command=main.destroy).pack()
for i in range(1,100):
    tk.Label(main,text=i,background="blue",width=results[i],anchor="w",height=1,fg="red",justify="left",font=1).pack()
main.mainloop()