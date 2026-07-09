from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("375x400")

# Entry Box
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# created the function perform
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0,str(result) + str(num))

# Buttons
b= Button(window, text='1',width=12,command=lambda:click(1))
b.place(x=10, y=60)

b= Button(window, text='2',width=12, command=lambda:click(2))
b.place(x=80, y=60)

b= Button(window, text='3',width=12, command=lambda:click(3))
b.place(x=170, y=60)

b= Button(window, text='4',width=12,command=lambda:click(4))
b.place(x=10, y=120)

b= Button(window, text='5',width=12,command=lambda:click(5))
b.place(x=80, y=120)

b= Button(window, text='6',width=12,command=lambda:click(6))
b.place(x=170, y=120)

b= Button(window, text='7',width=12,command=lambda:click(7))
b.place(x=10, y=180)

b= Button(window, text='8',width=12,command=lambda:click(8))
b.place(x=80, y=180)

b= Button(window, text='9',width=12,command=lambda:click(9))
b.place(x=170, y=180)

b= Button(window, text='0',width=12,command=lambda:click(0))
b.place(x=10, y=240)

#Operator
# def add():
#     n1 = e.get()
#     global matt
#     matt = "Addition"
#     i = int(n1)


def add():
    global i
    global matt
    n1 = e.get()
    i = int(n1)
    matt = "Addition"
    e.delete(0, END)

b= Button(window, text='+',width=12, command = add)
b.place(x=80, y=240)

def sub():
    n1 = e.get()
    global matt
    global i
    matt = "substraction"
    i = int(n1)
    e.delete(0, END)

b= Button(window, text='-',width=12, command = sub)
b.place(x=170, y=240)

def mul():
    n1 = e.get()
    global matt
    global i
    matt = "Multiplication"
    i = int(n1)
    e.delete(0, END)

b= Button(window, text='*',width=12, command = mul)
b.place(x=10, y=300)

def div():
    n1 = e.get()
    global matt
    global i
    matt = "Division"
    i = int(n1)
    e.delete(0, END)

b= Button(window, text='/',width=12,command = div)
b.place(x=70, y=300)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if matt == "Addition":
        e.insert(0,i + int(n2))
    elif matt == "substraction":
        e.insert(0,i - int(n2))
    elif matt == "Multiplication":
        e.insert(0,i * int(n2))
    elif matt == "Division":
        e.insert(0,i / int(n2))

b= Button(window, text='=',width=12,command= equal)
b.place(x=170, y=300)

def clear():
    e.delete(0, END)

b= Button(window, text='Clear',width=12,command = clear)
b.place(x=10, y=350)

#  steps 4: mainloop
window.mainloop()