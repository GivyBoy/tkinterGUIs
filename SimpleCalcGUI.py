from tkinter import *

root = Tk()
root.title('Simple Calculator GUI')


def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def Clear():
    e.delete(0, END)


def add():
    firstNum = e.get()
    global fNum
    fNum = int(firstNum)
    e.delete(0, END)


def equal():
    secNum = e.get()
    e.delete(0, END)
    e.insert(0, fNum + int(secNum))


e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button1 = Button(root, text='1', padx=40, pady=10, command=lambda: buttonClick(1))
button2 = Button(root, text='2', padx=40, pady=10, command=lambda: buttonClick(2))
button3 = Button(root, text='3', padx=40, pady=10, command=lambda: buttonClick(3))
button4 = Button(root, text='4', padx=40, pady=10, command=lambda: buttonClick(4))
button5 = Button(root, text='5', padx=40, pady=10, command=lambda: buttonClick(5))
button6 = Button(root, text='6', padx=40, pady=10, command=lambda: buttonClick(6))
button7 = Button(root, text='7', padx=40, pady=10, command=lambda: buttonClick(7))
button8 = Button(root, text='8', padx=40, pady=10, command=lambda: buttonClick(8))
button9 = Button(root, text='9', padx=40, pady=10, command=lambda: buttonClick(9))
button0 = Button(root, text='0', padx=40, pady=10, command=lambda: buttonClick(0))
buttonClear = Button(root, text='Clear', padx=85, pady=10, command=Clear)
buttonEqual = Button(root, text='=', padx=95, pady=10, command=equal)
buttonAdd = Button(root, text='+', padx=39, pady=10, command=add)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

root.mainloop()
