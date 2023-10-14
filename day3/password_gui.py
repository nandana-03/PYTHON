import tkinter as tk
import random
def pw():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password=[]
    for i in range(0,5):
        password.append(random.choice(letters))
    for i in range(0,3):
        password.append(random.choice(numbers))
    for i in range(0,2):
        password.append(random.choice(symbols))
        
    random.shuffle(password)

    org=""
    for i in password:
        org+=i

    label.config(text=f"Your newly generated password is {org}")


window=tk.Tk()
window.title("Password Generator")
window.minsize(500,300)
window.configure(bg='#022e64')
"""
Gird.rowconfigure(window,1,1)
Gird.rowconfigure(window,5,1)
Gird.rowconfigure(window,10,1)
"""
label1=tk.Label(text="Welcome to Password Generator!!",font="Georgia")
label1.grid(row=1,column=3)


button=tk.Button(text="Generate password",font="Georgia",command=pw)
button.grid(row=5,column=3)


label=tk.Label(text="Password here",font="Georgia")
label.grid(row=10,column=3)


window.mainloop()