from tkinter import *
import timer2

#create a root window
root = Tk()
root.title("Computer Timer")
root.geometry("500x150")

#create a frame in the window to hold other widgets
app = timer2.Application(root)

#enter root event loop
root.mainloop()
