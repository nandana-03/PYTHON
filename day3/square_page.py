import tkinter as tk
window=tk.Tk()
window.title("Square of numbers")
window.minsize(500,500)

input=tk.Entry()
input.pack()
input.place(x=180,y=30)

def on_click():
    n=float(input.get())
    num=n*n
    label.config(text=num)

button=tk.Button( text="Submit",font="Georgia",command=on_click)
button.pack()
button.place(x=200,y=60)

label=tk.Label(text="Result")
label.pack(side="bottom")

    
window.mainloop()
