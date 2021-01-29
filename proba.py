from tkinter import *

class Application():
    lista = [11.5, 10.2, 10, 13, 11.1, 13.2, 13.4, 10.4, 11.3, 14.4, 11.2, 12.3, 10.5, 14.2, 15.5, 14.3, 9.3, 12.4, 9, 10, 14.2, 15.2, 10.3, 14.3, 10, 14.5, 8.2, 14, 13, 12.4, 12.2, 11.5, 15.3, 11.5, 13.5, 12.4, 8.5, 11.3, 12.2, 9.1, 11.2, 12.5, 14.4, 13, 15.3, 12.5, 9.1, 14.3, 12.1, 9.2]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = MyRootDialog.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()

    def say_hi(self):
        print("hi there, everyone!")

