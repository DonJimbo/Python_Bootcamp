from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig (timer_text, text = "00:00")
    label_a.config (text= "Timer")
    label_b.config (text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_a.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        label_a.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        label_a.config(text="Work", fg=GREEN)
        count_down(work_sec)


    '''Alternative'''

    # while reps < 9:
    #    # If it's the 1st/3rd/5th/7th rep:
    #    if reps in {0, 2, 4, 3, 4, 6}:
    #        reps += 1
    #        print(reps)
    #        return count_down(work_sec)

    #    # If it's the 1st/3rd/5th/7th rep:
    #    if reps in {1, 3, 5, 7}:
    #        reps += 1
    #        print(reps)
    #        return count_down(short_break_sec)

    #    # If it's the 8th rep:
    #    if reps == 8:
    #        return count_down(long_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅"
        label_b.config(text = mark)

'''Alternative'''

#   import time
#   count = 5
#   while True:
#       time.sleep(1)
#       count -= 1

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg=YELLOW)

label_a = Label(text="Timer", font=(FONT_NAME, 50, "bold",), fg=GREEN, bg=YELLOW)
label_a.grid(column=1, row=0)

label_b = Label(fg = GREEN, bg=YELLOW)
label_b.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(99.5,112,image = tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00",fill= "white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

button_a = Button(text = "Start", highlightthickness = 0, command = start_timer)
button_a.grid(column=0, row=2)

button_b = Button(text = "Reset", highlightthickness = 0, command= reset_timer)
button_b.grid(column=2, row=2)

window.mainloop()