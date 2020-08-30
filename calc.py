import tkinter
from tkinter import *

root = Tk()
root.title('Calculator')
root.config(bg = 'lightgreen')
e = Entry(root, width = 55,borderwidth = 5, font = ('Arial', 10, 'bold'))
e.grid(row=0,column=0, columnspan = 4, padx = 10, pady = 20, ipady = 20)

def button_clicked(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_point():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + ".")

def btn_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)

def button_per():
    first_number = e.get()
    global f_num
    global math
    math = "remainder"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0, f_num + float(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - float(second_number))
    if math == 'multiply':
        e.insert(0, f_num * float(second_number))
    if math == 'divide':
        e.insert(0, f_num / float(second_number))
    if math == 'remainder':
        e.insert(0, f_num % float(second_number))

btn1 = Button(root, text = "1", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(1))
btn2 = Button(root, text = "2", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(2))
btn3 = Button(root, text = "3", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(3))
btn4 = Button(root, text = "4", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(4))
btn5 = Button(root, text = "5", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(5))
btn6 = Button(root, text = "6", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(6))
btn7 = Button(root, text = "7", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(7))
btn8 = Button(root, text = "8", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(8))
btn9 = Button(root, text = "9", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(9))
btn0 = Button(root, text = "0", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = lambda : button_clicked(0))
btnadd = Button(root, text = "+", padx = 30, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_add)
btnsub = Button(root, text = "-", padx = 33, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_sub)
btnmul = Button(root, text = "*", padx = 31, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_mul)
btndiv = Button(root, text = "/", padx = 32, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_div)
btnper = Button(root, text = "%", padx = 28, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_per)
btnpoint = Button(root, text = ".", padx = 32, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_point)
btnequal = Button(root, text = "=", padx = 80, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = button_equal)
btnclear = Button(root, text = "C", padx = 80, pady = 20, bd = 5, bg = 'lightblue', font = ('Arial', 16, 'bold'), command = btn_clear)

btn7.grid(row = 1, column = 0)
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)

btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)

btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)

btn0.grid(row = 4, column = 0)

btnadd.grid(row = 1, column = 3)
btnsub.grid(row = 2, column = 3)
btnmul.grid(row = 3, column = 3)
btndiv.grid(row = 4, column = 3)

btnper.grid(row = 4, column = 2)
btnpoint.grid(row = 4, column = 1)
btnequal.grid(row = 5, column = 0, columnspan = 2)
btnclear.grid(row = 5, column = 2, columnspan = 2)

root.mainloop()