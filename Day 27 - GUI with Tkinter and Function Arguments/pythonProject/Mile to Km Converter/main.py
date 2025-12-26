from tkinter import *

def miles_to_km ():
    miles = float(input_number.get())
    km = round(miles * 1.689,2)
    label_d.config(text= f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=40,pady=20)

label_a = Label(text="Miles")
label_b = Label(text="Km")
label_c = Label(text="is equal to")
label_d = Label(text= "0")
input_number = Entry()
button = Button(text="Calculate", command= miles_to_km)

label_a.grid (row = 0, column = 2)
label_b.grid (row = 1, column = 2)
label_c.grid (row = 1, column = 0)
label_d.grid (row = 1, column = 1)
input_number.grid (row = 0, column = 1)
button.grid (row = 2, column = 1)

window.mainloop()