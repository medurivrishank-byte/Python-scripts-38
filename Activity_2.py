from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Virus scan")
window.geometry("200x200")
def message():
    messagebox.showwarning("Alert!","Stop! Virus found")
button=Button(window,text="Scan for virus",command=message)
button.place(x=40,y=40)
window.mainloop()