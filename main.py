from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
check_mark_num = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- #
# def minute_and_sec():
#     sec = count * 60
#     minute = count
def start_timer():
    global reps, check_mark_num
    reps += 1
    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN
    if reps == 1:
        pass
    else:
        chck_mark = ""
        for ch in range(check_mark_num):
            chck_mark += "✔"
        chek_box_label.config(text=chck_mark)
    # checkmark update
    # check_mark_list = []
    # for _ in range(reps % 4):
    #     check_mark_list.append("✔")
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text= "Break", fg= PINK)
        check_mark_num = 0
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text= "Break", fg=RED)
    elif reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text= "Work", fg=GREEN)
        check_mark_num += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 




def count_down(count):

    count_mnt = math.floor(count/60)
    count_sec = count % 60
    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_mnt}:{count_sec}")
    # print(count)
    if count > 0:
        window.after(50, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image= tomato_img)
timer_text = canvas.create_text(100, 140, text= "00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)



timer_label = Label(text="Timer",bg= YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)


chek_box_label = Label(text="", bg= YELLOW, highlightthickness=0, fg=GREEN, font=(FONT_NAME, 20, "bold"))
chek_box_label.grid(row=3, column=1)
start_button = Button(text="Start", command= start_timer)
start_button.grid(row=2, column=0)
finish_button = Button(text="Finish")
finish_button.grid(row=2, column=2)












window.mainloop()




