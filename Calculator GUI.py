from tkinter import *

root = Tk()
root.title("Sample Calculator")
# entry section
myEntry = Entry(root, width=35, borderwidth=5)
myEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
myEntry.focus_set()


# function section
def Button_Click(number):
    currentClick = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(currentClick) + str(number))


def Button_Clear():
    myEntry.delete(0, END)


def Button_addition():
    firstNumber = myEntry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(firstNumber)
    myEntry.delete(0, END)


def Button_subtraction():
    firstNumber = myEntry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(firstNumber)
    myEntry.delete(0, END)


def Button_multiplication():
    firstNumber = myEntry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(firstNumber)
    myEntry.delete(0, END)


def Button_division():
    firstNumber = myEntry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(firstNumber)
    myEntry.delete(0, END)


def Button_equal():
    second_num = myEntry.get()
    myEntry.delete(0, END)

    if math == 'addition':
        myEntry.insert(0, int(f_num) + int(second_num))
    elif math == 'subtraction':
        myEntry.insert(0,int(f_num) - int(second_num))
    elif math == 'multiplication':
        myEntry.insert(0,int(f_num) * int(second_num))
    elif math == 'division':
        myEntry.insert(0,int(f_num) / int(second_num))


# button section
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: Button_Click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: Button_Click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: Button_Click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: Button_Click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: Button_Click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: Button_Click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: Button_Click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: Button_Click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: Button_Click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: Button_Click(0))

button_add = Button(root, text='+', padx=39, pady=20, command=Button_addition)
button_sub = Button(root, text='-', padx=40, pady=20, command=Button_subtraction)
button_mul = Button(root, text='*', padx=40, pady=20, command=Button_multiplication)
button_div = Button(root, text='/', padx=40, pady=20, command=Button_division)

button_eq = Button(root, text='=', padx=91, pady=20, command=Button_equal)
button_cl = Button(root, text='Clear', padx=79, pady=20, command=Button_Clear)

# put the button on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)
button_eq.grid(row=5, column=1, columnspan=2)
button_cl.grid(row=4, column=1, columnspan=2)

root.mainloop()
