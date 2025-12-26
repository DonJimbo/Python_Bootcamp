import tkinter
from tkinter import Entry

from pythonProject.Theory.Other_Tkinter_Widgets import entry

window = tkinter.Tk()
window.title ("My First GUI Program")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="I am a Label", font=("Arial", 24,"bold"))
my_label.grid (column = 1, row = 1)

my_label["text"] = "New Text"
my_label.config(text = "New Text")

entry_a = Entry()
entry_a.grid (column = 4, row = 4)

def button_clicked():
    new_text = entry_a.get()
    print(new_text)
    my_label.config(text = new_text)

button_a = tkinter.Button(text="Click Me", command=button_clicked)
button_a.grid (column = 2, row = 2)

button_b = tkinter.Button(text="2 button")
button_b.grid (column = 3, row = 1)

window.mainloop()
