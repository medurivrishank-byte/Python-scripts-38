from tkinter import *
window=Tk()
window.title("Event handler")
window.geometry("100x100")
def handle_keypress(event):
    '''Print the character according to the key pressed'''
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("\nThe button was clicked!")
btn=Button(text="Click here")
btn.pack()
btn.bind("<Button-1>",handle_click)
window.mainloop()