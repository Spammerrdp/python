import time # pip install time
from tkinter import * # pip install tk
root = Tk()
root.title("Digital clock")
def current():
        ctime = time.strftime("%H : %M : %S ")
        lable.config(text=ctime)
        lable.after(60,current)
lable = Label(root,font=("Bold",100),background="white",foreground="grey")
lable.pack()
current()
root.mainloop()
