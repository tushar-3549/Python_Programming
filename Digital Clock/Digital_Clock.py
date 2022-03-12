import time
from tkinter import *

root = Tk()
root.title("Digital Clock")
root.configure(background='black')


def start():
    txt = time.strftime("%H:%M:%S")
    Label.config(text=txt)
    Label.after(200, start) #200 mili second


Label = Label(root, font=("ds_digital", 101), fg='red', bg='black') #font(font_name,font_size)
Label.grid(row=0, column=0)
start()
root.mainloop()
