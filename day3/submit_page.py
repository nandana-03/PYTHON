import tkinter as tk
window=tk.Tk()
window.title("Submit")
window.minsize(500,500)

input=tk.Entry()
input.grid(column=2,row=0, padx=0, pady=0, sticky="NSEW")

def on_click():
    txt=input.get()
    label.config(text=txt)
    #print(text)

button=tk.Button( text="Submit",font="Georgia",command=on_click)
button.grid(column=2,row=2, padx=0, pady=0, sticky="NSEW")


label=tk.Label(text="Your name here")
label.grid(column=2,row=3, padx=0, pady=0, sticky="NSEW")
 
window.mainloop()