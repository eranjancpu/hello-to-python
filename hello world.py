from tkinter import *

root = Tk()

def seeMore():
    num5 = Label(root, text="5").grid(row=5, column=5)
    num6 = Label(root, text="6").grid(row=6, column=6)
    num7 = Label(root, text="7").grid(row=7, column=7)
    num8 = Label(root, text="8").grid(row=8, column=8)

num0 = Label(root, text="0").grid(row=0, column=0)
num1 = Label(root, text="1").grid(row=1, column=1)
num2 = Label(root, text="2").grid(row=2, column=2)
num3 = Label(root, text="3").grid(row=3, column=3)
num4 = Label(root, text="4").grid(row=4, column=4)
butt1 = Button(root, text="click me to see more", padx=10, pady=10, command=seeMore, bg="red").grid(row=0, column=5)

root.mainloop()
