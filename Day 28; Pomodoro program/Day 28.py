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
    global reps
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps == 8:
        countdown(long_break_seconds)
        title_label.config(text="Break", fg=RED)
        reps = 1
    elif reps % 2 == 0:
        countdown(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_seconds)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds <= 9:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "🗸"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer_label
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# start button
start_button = Button(text="Start", bg="white", width=2, height=1, command=start_timer)
start_button.grid(column=0, row=2)

# checkmarks
checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmark.grid(column=1, row=3)

# reset button
reset_button = Button(text="Reset", bg="white", width=2, height=1, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
