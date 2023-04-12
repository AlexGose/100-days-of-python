import tkinter
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

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 or reps % 8 == 2 or reps % 8 == 4 or reps % 8 == 6:
        reps += 1
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 7:
        reps += 1
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        reps += 1
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        window.after(10, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks_label.config(text="✔" * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(row=2, column=2)

checks_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
checks_label.grid(row=2, column=1)

window.mainloop()
