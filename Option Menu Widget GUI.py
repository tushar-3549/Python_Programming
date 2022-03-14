from tkinter import *

root = Tk()
root.title("Option Menu")
root.geometry("600x600")
textVar = StringVar()
textVar.set("Tushar")


# print(textVar.get())
def show():
    selected = textVar.get()
    if selected == "Tushar":
        lab = Label(root, text="Het ! You selected Tushar")
        lab.pack()
    else:
        lab = Label(root, text=textVar.get())
        lab.pack()
    # label = Label(root,textVar.get())
    # label.pack()


drop_menu = OptionMenu(root, textVar, "Tushar", "Maruf", "Sakib")
drop_menu.pack()
btn = Button(root, text="show result", command=show)
btn.pack()
root.mainloop()
