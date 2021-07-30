from tkinter import *

root = Tk()
root.title('Simple Calculator')
myEntry= Entry(root, width= 45, borderwidth=5);
myEntry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
myEntry.insert(1, 'Enter your value')

def buttonAdd():
    return
def buttonClick(number):
    current=myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(current)+str(number))

def buttonClear():
    myEntry.delete(0, END)

def buttonAdd():
    first_num=myEntry.get()
    global f_num
    global math
    math='add'
    f_num= int(first_num)
    myEntry.delete(0, END)
def buttonSub():
    first_num=myEntry.get()
    global f_num
    global math
    math='sub'
    f_num= int(first_num)
    myEntry.delete(0, END)
def buttonMul():
    first_num=myEntry.get()
    global f_num
    global math
    math='mul'
    f_num= int(first_num)
    myEntry.delete(0, END)
def buttonDiv():
    first_num=myEntry.get()
    global f_num
    global math
    math='div'
    f_num= int(first_num)
    myEntry.delete(0, END)

def buttonEqual():
    second_num=myEntry.get()
    myEntry.delete(0, END)
    if math == 'add':
        myEntry.insert(0, f_num + int(second_num))
    if math == 'sub':
        myEntry.insert(0, f_num - int(second_num))
    if math == 'mul':
        myEntry.insert(0, f_num * int(second_num))
    if math == 'div':
        myEntry.insert(0, f_num / int(second_num))

button1 = Button(root, command= lambda: buttonClick(1), text="1", padx=40, pady=20);
button2 = Button(root, command= lambda: buttonClick(2), text="2", padx=40, pady=20);
button3 = Button(root, command= lambda: buttonClick(3), text="3", padx=40, pady=20);
button4 = Button(root, command= lambda: buttonClick(4), text="4", padx=40, pady=20);
button5 = Button(root, command= lambda: buttonClick(5), text="5", padx=40, pady=20);
button6 = Button(root, command= lambda: buttonClick(6), text="6", padx=40, pady=20);
button7 = Button(root, command= lambda: buttonClick(7), text="7", padx=40, pady=20);
button8 = Button(root, command= lambda: buttonClick(8), text="8", padx=40, pady=20);
button9 = Button(root, command= lambda: buttonClick(9), text="9", padx=40, pady=20);
button0 = Button(root, command= lambda: buttonClick(0), text="0", padx=40, pady=20);
button_equal=Button(root, command= buttonEqual, text='=', padx=39, pady=72);
button_add=Button(root, command= buttonAdd, text='+', padx=39, pady=20);
button_sub=Button(root, command= buttonSub, text='-', padx=41, pady=20);
button_mul=Button(root, command= buttonMul, text='*', padx=40, pady=20);
button_div=Button(root, command= buttonDiv, text='÷', padx=40, pady=20);
button_clear=Button(root, command= buttonClear, text='Clear', padx=29.5, pady=20);

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4, column=0)
button_equal.grid(row=4,column=2, rowspan=3)
button_clear.grid(row=4,column=1)
button_add.grid(row=5,column=0)
button_sub.grid(row=5,column=1)
button_mul.grid(row=6,column=0)
button_div.grid(row=6,column=1)

root.mainloop()
