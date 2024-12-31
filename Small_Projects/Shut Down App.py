from tkinter import *
import os


def restart():
    os.system("shutdown -r -t 1")


def restart_time():
    os.system("shutdown -r -t 20")


def shutdown():
    os.system("shutdown -s -t 1")


window = Tk()
window.title("Shut down App")
window.geometry("500x500")
window.config(bg="blue")

# Restart button
r_button = Button(window, text="Restart", font=("Ubuntu", 20, "bold"), bg="red", cursor="plus", command=restart)
r_button.place(x=150, y=60, width=200, height=50)
# Restart time
r_button = Button(window, text="Restart Time", font=("Ubuntu", 20, "bold"), bg="red", cursor="plus",
                  command=restart_time)
r_button.place(x=150, y=170, width=200, height=50)
# shut down
r_button = Button(window, text="Shut down", font=("Ubuntu", 20, "bold"), bg="red", cursor="plus", command=shutdown)
r_button.place(x=150, y=270, width=200, height=50)
# close button
r_button = Button(window, text="Exit", font=("Ubuntu", 20, "bold"), bg="red", cursor="arrow", command=window.destroy)
r_button.place(x=150, y=370, width=200, height=50)

window.mainloop()

# Here , x = left to right  , y = Top to botom


#Md Tushar Ahmed --> Bye
