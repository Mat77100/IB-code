#secondary file
import tkinter as tk
from remoteOOPmain import remoteCtrlBtn as btn
#attributes available: appName, btnID, appID
#methods available: press()

ntflx = btn("Netflix", 1, 14)
yt = btn("Youtube", 2, 27)
amzn = btn("Amazon", 3, 8)
apl = btn("Apple", 4, 2)

remote = tk.Tk(className = "Remote")
btn1 = tk.Button(remote,text = "Netflix", command = ntflx.press,font=50,bg="red",height = 3, width = 10)
btn2 = tk.Button(remote,text = "Youtube", command = yt.press,font=50,bg="orange",height = 3, width = 10)
btn3 = tk.Button(remote,text = "Amazon", command = amzn.press,font=50,bg="blue",height = 3, width = 10)
btn4 = tk.Button(remote,text = "Apple", command = apl.press,font=50,bg="lightgrey",height = 3, width = 10)

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

remote.mainloop()