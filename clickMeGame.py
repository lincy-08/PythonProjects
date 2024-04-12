import tkinter
from tkinter import Button
import random

'''Try to click the clickme Button '''

class clickmegame():

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("500x500")

        self.clickme = Button(self.window, text="clickme")
        self.clickme.place(x=20, y=30)
        self.clickme.bind("<Enter>",self.move)
        self.window.mainloop()

    def move(self,event):
        self.clickme.place(x=random.random() * 500, y=random.random() * 500)



game = clickmegame()

