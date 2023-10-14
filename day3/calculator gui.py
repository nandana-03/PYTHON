import tkinter as tk

window=tk.Tk()
window.title("Calculator")
window.minsize(300,300)

expression = ""
input_text = tk.StringVar()

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = "" 
    input_text.set("")

 
def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)

  
input1 = tk.Entry(textvariable = input_text,width = 50)
input1.grid(row=0, column=0, padx=0, columnspan=4, pady=0, sticky="NSEW")
 
clear = tk.Button( text = "C", width = 35, height = 3,command = lambda:bt_clear())
clear.grid(row = 1, column = 0, columnspan=3, padx=0, pady=0, sticky="NSEW")

divide = tk.Button(text = "/", width = 5, height = 3,command =lambda:btn_click("/"))
divide.grid(row = 2, column = 3, padx=0, pady=0, sticky="NSEW")

seven = tk.Button(text = "7",width = 5, height = 3,command =lambda:btn_click(7))
seven.grid(row = 2, column = 0, padx=0, pady=0, sticky="NSEW")

eight = tk.Button(text = "8",width = 5, height = 3,command =lambda:btn_click(8))
eight.grid(row = 2, column = 1, padx=0, pady=0, sticky="NSEW")

nine = tk.Button(text = "9", width = 5, height = 3,command =lambda:btn_click(9))
nine.grid(row = 2, column = 2, padx=0, pady=0, sticky="NSEW")
 
multiply = tk.Button(text = "*",width = 5, height = 3,command =lambda:btn_click("*"))
multiply.grid(row = 3, column = 3, padx=0, pady=0, sticky="NSEW")

four =tk.Button(text = "4",width = 5, height = 3,command =lambda:btn_click(4))
four.grid(row = 3, column = 0, padx=0, pady=0, sticky="NSEW")
 
five =tk.Button(text = "5",width = 5, height = 3,command =lambda:btn_click(5))
five.grid(row = 3, column = 1, padx=0, pady=0, sticky="NSEW")
 
six =tk.Button(text = "6",width = 5, height = 3,command =lambda:btn_click(6))
six.grid(row = 3, column = 2, padx=0, pady=0, sticky="NSEW")

minus =tk.Button(text = "-",width = 5, height = 3,command =lambda:btn_click("-"))
minus.grid(row = 4, column = 3, padx=0, pady=0, sticky="NSEW")
 
one =tk.Button(text = "1",width = 5, height = 3,command =lambda: btn_click(1))
one.grid(row = 4, column = 0, padx=0, pady=0, sticky="NSEW")
 
two =tk.Button(text = "2",width = 5, height = 3,command =lambda:btn_click(2))
two.grid(row = 4, column = 1, padx=0, pady=0, sticky="NSEW")
 
three =tk.Button(text = "3",width = 5, height = 3,command =lambda:btn_click(3))
three.grid(row = 4, column = 2, padx=0, pady=0, sticky="NSEW")
 
plus =tk.Button(text = "+",width = 5, height = 3,command =lambda:btn_click("+"))
plus.grid(row = 5, column = 3, padx=0, pady=0, sticky="NSEW")

zero = tk.Button(text = "0",width = 5, height = 3,command = lambda: btn_click(0))
zero.grid(row = 5, column = 0, columnspan=2, padx=0, pady=0, sticky="NSEW")
 
point = tk.Button(text = ".",width = 5, height = 3,command = lambda: btn_click("."))
point.grid(row = 5, column = 2, padx=0, pady=0, sticky="NSEW")
 
equals = tk.Button(text = "=",width = 5, height = 3,command = lambda: bt_equal())
equals.grid(row = 1, column = 3, padx=0, pady=0, sticky="NSEW")

window.mainloop()
