import tkinter,math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
clock=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(clock)
    check['text'] = " "
    Header['text'] = "Timer"
    canvas.itemconfig(timer,text="00:00")
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_Sec=WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%8 ==0:
        count_down(long_break_sec)
        Header['text']="Break"
    elif reps%2==0:
        count_down(short_break_sec)
        Header['text'] = "Break"
    else:
        count_down(work_Sec)
        Header['text'] = "Work"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps,clock
    minutes=math.floor(count/60)
    seconds=count%60
    if seconds<10:
        seconds=f"0{seconds}"
    canvas.itemconfig(timer,text=f"{minutes}:{seconds}")
    if count>0:
        clock=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in  range(math.floor(reps/2)):
            mark+="✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window=tkinter.Tk()
window.minsize(width=500,height=400)
window.config(padx=60,pady=60,bg=GREEN)

Header=tkinter.Label()
Header['text']="Timer"
Header['fg']=YELLOW
Header['bg']=GREEN
Header['font']=(FONT_NAME,25,"bold")
Header.grid(column=1,row=0)


canvas=tkinter.Canvas(width=220,height=230,bg=GREEN,highlightthickness=0)
img=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(110,115,image=img)
timer=canvas.create_text(110,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

Start=tkinter.Button(command=start_timer)
Start['text']="Start"
Start['font']=(FONT_NAME,15,"bold")
Start.grid(column=0,row=2)


check=tkinter.Label()
check['text']=" "
check['bg']=GREEN
check['font']=(FONT_NAME,15,"bold")
check.grid(column=1,row=3)

Reset=tkinter.Button(command=reset_timer)
Reset['text']="Reset"
Reset['font']=(FONT_NAME,15,"bold")
Reset.grid(column=2,row=2)

window.mainloop()