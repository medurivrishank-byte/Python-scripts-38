from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Tkinter messagebox guide")
window.geometry("300x150")
def show_info():
    messagebox.showinfo("Success","Operation completed successfuly")
def ask_confirmation():
    response=messagebox.askyesno("Exit","Are you sure you want to quit?")
    if response:
        window.destroy()
btn_info=Button(window,text="Trigger alert",command=show_info)
btn_info.pack(pady=10)
btn_exit=Button(window,text="Close app",command=ask_confirmation)
btn_exit.pack(pady=10)
window.mainloop()