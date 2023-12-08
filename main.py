from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer_text
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer", fg = GREEN)
    checkbox_label.config(text = " ")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 2 == 0:
        timer_label.config(text = "SHORT BREAK 5 MIN", fg= PINK)
        count_down ( short_break_sec)
    elif reps % 8 == 0:
        timer_label.config ( text = "LONG BREAK 20 MIN" , fg = RED )
        count_down(long_break_sec)
    else:
        timer_label.config ( text = "WORK FOR 25 MIN" , fg = GREEN )
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min =math.floor(count / 60)
    count_sec =  count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after (10 , count_down , count - 1 )
    else:
        start_timer()
        marks = "✓"
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            checkbox_label.config(text = marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx =100 , pady =50, bg= YELLOW )


timer_label = Label(text = "Timer", font = (FONT_NAME, 39, "bold"), fg =GREEN , bg = YELLOW )
timer_label.grid(column = 6, row =0 )

canvas = Canvas(width = 200, height = 224, bg = YELLOW)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(103, 112, image = tomato_img)
timer_text = canvas.create_text(110, 132, text = "00:00", fill = "white", font = (FONT_NAME, 24, "bold"))
canvas.grid(column =6 , row =12 )


start_button = Button(text = "start", font = (FONT_NAME, 10, "bold"), fg =RED , bg = YELLOW , command = start_timer)
start_button.grid(column = 2, row =22 )

reset_button = Button(text = "reset", font = (FONT_NAME, 10, "bold"), fg =RED , bg = YELLOW , command = timer_reset)
reset_button.grid(column = 8, row =22 )

checkbox_label = Label(fg =GREEN , bg = YELLOW )
checkbox_label.grid(column = 6, row =24 )



# canvas.pack()







window.mainloop()