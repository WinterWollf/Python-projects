from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
stage = 1
check_marks_list = []
timer_machine = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global check_marks_list, stage
    window.after_cancel(timer_machine)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", foreground=GREEN)
    check_marks_list.clear()
    check_marks.config(text="")
    stage = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_counting():
    global stage
    if stage == 1 or stage == 3 or stage == 5 or stage == 7:
        stage += 1
        count_down(WORK_MIN * 60)
        timer.config(text="Work", foreground=RED)
    elif stage == 2 or stage == 4 or stage == 6:
        stage += 1
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", foreground=PINK)
    elif stage == 8:
        stage += 1
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break", foreground=GREEN)
    else:
        stage = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer_machine
        timer_machine = window.after(1000, count_down, count - 1)
    else:
        if stage == 3 or stage == 5 or stage == 7 or stage == 8:
            check_marks_list.append("✔")
            check_marks.config(text=check_marks_list)

        start_counting()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=500, height=400)
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

timer = Label()
timer.config(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 40, "bold"))
timer.grid(column=1, row=0)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_1 = Button()
button_1.config(text="Start", command=start_counting)
button_1.grid(column=0, row=2)
button_2 = Button()
button_2.config(text="Reset", command=reset)
button_2.grid(column=2, row=2)

check_marks = Label()
check_marks.config(foreground=GREEN, background=YELLOW, highlightthickness=0)
check_marks.grid(column=1, row=3)


window.mainloop()
