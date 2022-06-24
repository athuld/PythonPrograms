from tkinter import *

root = Tk()

root.geometry("100x100")

def exit_window():
    exit()

btn = Button(root,text="exit",bd=2,command=exit_window)
btn.pack(side='top')
root.mainloop()


