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
def resetTimer(): 
    global reps 
    global timer
    window.after_cancel(timer)
    timerLabel.config(text='Timer')
    canvas.itemconfig(timerText, text='00:00')
    check.config(text='', fg=GREEN)

    
    reps = 0 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer(): 
    global reps 
    work  = WORK_MIN  
    shortBreak = SHORT_BREAK_MIN 
    longBreak = LONG_BREAK_MIN 

    reps += 1

    if reps % 8 == 0: 
        timerLabel.config(text="25 Minute Break", fg=RED)
        countDown(longBreak) 
    elif reps % 2 == 0: 
        timerLabel.config(text="5 Minute Break", fg=PINK)
        countDown(shortBreak) 
    else: 
        timerLabel.config(text="Work", fg=GREEN)

        countDown(work) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count): 
    global timer 
    #formulating the count string 
    countMin = math.floor(count/60)
    countSec = count % 60
    if countSec == 0: 
        countSec = '00'

    elif countSec < 10: 
        countSec = '0' + str(countSec)

    totalCount = str(countMin) + ':' + str(countSec)

    #adding count to canvas
    canvas.itemconfig(timerText, text=totalCount)
    if count > 0: 
        timer = window.after(1000, countDown, count - 1)
    else: 
        
        mark = '' 
        if math.floor(reps % 2) == 0: 
            mark += '✓'
        
        check.config(text=mark, fg=GREEN)
        startTimer()

        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() 
window.title("Pomodoro") 
window.config(padx=100, pady=100, bg=YELLOW)

#create timer label 
timerLabel = Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timerLabel.grid(row=0, column=1)

#create canvas 
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) 
Photo = PhotoImage(file='tomato.png') 
canvas.create_image(100, 112, image=Photo) 
timerText = canvas.create_text(100, 130, text='00:00', fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1) 


#Start Button 
startButton = Button(text='Start', bg=YELLOW, command=startTimer) 
startButton.grid(row=3, column=0)


#Reset Button 
resetButton = Button(text='Reset', bg=YELLOW, command=resetTimer) 
resetButton.grid(row=3, column=2)

#CheckMark
check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=4, column=1)
window.mainloop()