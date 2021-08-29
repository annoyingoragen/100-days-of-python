import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quizinterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=50,pady=20)

        self.window.minsize(width=700,height=600)

        self.Score=tkinter.Label(text="Score:0",bg=THEME_COLOR,font=("Arial",20))
        self.Score.grid(row=0,column=1,sticky='e')

        self.canvas=tkinter.Canvas(bg="white",height=300,width=600)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=40)

        self.canvas_text=self.canvas.create_text(300,150,width=500,text="ngjh",font=("Arial",20,'italic'))

        correctimage=tkinter.PhotoImage(file="images/true.png")
        self.correctbutton=tkinter.Button(image=correctimage,command=self.statement_is_true)
        self.correctbutton.grid(row=2,column=0)

        incorrectimage=tkinter.PhotoImage(file="images/false.png")
        self.incorrectbutton=tkinter.Button(image=incorrectimage,command=self.statement_is_false)
        self.incorrectbutton.grid(row=2,column=1)
        self.getting_next_question_text_in_ui()
        self.window.mainloop()


    def getting_next_question_text_in_ui(self):
        q_text= self.quiz.next_question()
        if q_text == False:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of quiz")
            self.correctbutton.config(state="disabled")
            self.incorrectbutton.config(state="disabled")
        else:
            self.canvas.itemconfig(self.canvas_text,text=q_text)
            self.Score.config(text=f"Score:{self.quiz.score}")
        self.canvas.config(bg="white")


    def statement_is_true(self):

        is_right=self.quiz.check_answer("true")
        self.feedback_by_changing_canvas_colour( is_right)

    def statement_is_false(self):

        is_right= self.quiz.check_answer("false")
        self.feedback_by_changing_canvas_colour( is_right)

    def feedback_by_changing_canvas_colour(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.getting_next_question_text_in_ui)

