from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Length converter app")
window.geometry("300x300")
inches_entry=Entry(window)
inches_entry.pack(pady=10)
def inches_to_cm(inches):
    return inches*2.54
def show_result():
    inches=float(inches_entry.get())
    result=inches_to_cm(inches)
    messagebox.showinfo("Result",str(result)+" cm")
btn=Button(window,text="Convert",command=show_result)
btn.pack(pady=10)
window.mainloop()