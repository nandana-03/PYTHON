import tkinter
window=tkinter.Tk()
window.title("Miles to kilometer")
window.minsize(500,300)
input_text = tkinter.StringVar()

label1=tkinter.Label(text="In miles",font="Georgia")
label1.grid(row=1,column=2)

input1=tkinter.Entry()
input1.grid(row=1,column=4)

label2=tkinter.Label(text="To kilometers",font="Georgia")
label2.grid(row=3,column=2)

input2=tkinter.Entry(textvariable=input_text)
input2.grid(row=3,column=4)

def on_click():
    n=float(input1.get())
    num=1.60934*n
    input_text.set(num)

button=tkinter.Button(text="Convert",font="Georgia",command=on_click)
button.grid(row=4,column=4)

window.mainloop()
