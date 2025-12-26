from tkinter import *

from Proyect.main import window

'''Tkinker canvas'''
# bg = color
# highlightthickness = the area around the image
canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112,image = tomato_img)
canvas.create_text(103, 130, text="00:00",fill= "white", font=("Courier",35, "bold"))

'''Tkinker canvas item configuration'''
timer_text = canvas.create_text(103, 130, text="00:00",fill= "white", font=("Courier",35, "bold"))
canvas.itemconfig (timer_text, text = "00:00")

'''To formalize an image into a canvas'''
tomato_img = PhotoImage(file="tomato.png")

'''To do an action after waiting certain time + its cancelation'''
window = Tk()

def say_something (Thing):
    global timer
    timer = window.after(1000, say_something, "Hello")

window.after_cancel(timer)