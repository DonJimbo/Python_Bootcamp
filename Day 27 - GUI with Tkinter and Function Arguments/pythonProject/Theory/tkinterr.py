import tkinter
from tkinter import Entry

# Object
window = tkinter.Tk()

# Title and size
window.title ("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24,"bold"))
# To center it (side = "x" or expand = center)
my_label.pack(side = "bottom", expand=True)

# Configure the text
my_label["text"] = "New Text"
my_label.config(text = "New Text")

# Button
def button_clicked ():
    print("I got clicked")

button = tkinter.Button(text = "Click Me", command=button_clicked)

# Gives the visual to the action (pack (subaction))
button.pack()

# Gives the visual in a special location
button.place(x = 0, y = 0)

# Gives the visual respecting a grid
button.grid(column = 0, row = 0)

# Entry (text box)
input = Entry(width=10)
input.pack()
print(input.get())

# To add padding
window.config(padx = 1, pady = 0)

# To maintain the loop
window.mainloop()

