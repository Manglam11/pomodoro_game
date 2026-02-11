from tkinter import *

from numpy.f2py.f90mod_rules import fgetdims2

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image= tomato_img)
canvas.create_text(100, 140, text= "00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer",bg= YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

chek_box_label = Label(text="✔", bg= YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 20, "bold"))
chek_box_label.grid(row=3, column=1)
start_button = Button(text="Start" )
start_button.grid(row=2, column=0)
finish_button = Button(text="Finish")
finish_button.grid(row=2, column=2)












window.mainloop()




