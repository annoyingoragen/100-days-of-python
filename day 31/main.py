BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
import tkinter,pandas,random
try:
    language_data = pandas.read_csv("data/Learning.csv")
except FileNotFoundError:
    language_data=pandas.read_csv("data/french_words.csv")

language_data_dict=language_data.to_dict()
#****************************SELECTING RANDOM WORDS****************************************
index=None
def random_word_selection():
    global index
    flip_timer=3000
    window.after_cancel(flip_timer)
    index=random.randint(0,len(language_data_dict['French']))
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(word,text=language_data_dict['French'][index],fill="black")
    canvas.itemconfig(title, text="French",fill="black")

    window.after(flip_timer,flip_card)

def remove_known_word():
    del language_data_dict['French'][index]

    del language_data_dict['English'][index]
    DF=pandas.DataFrame(language_data_dict)
    DF.to_csv("data/Learning.csv",index=False)
    random_word_selection()



def flip_card():
    canvas.itemconfig(canvas_img,image=back_img)
    canvas.itemconfig(word, text=language_data_dict['English'][index],fill="white")
    canvas.itemconfig(title, text="English",fill="white")





window=tkinter.Tk()
window.minsize(600,660)
window.config(bg=BACKGROUND_COLOR,padx=60,pady=30)
window.title('flashy')

canvas=tkinter.Canvas(width=800,height=530,bg=BACKGROUND_COLOR,highlightthickness=0)
front_img=tkinter.PhotoImage(file="images\card_front.png")
back_img=tkinter.PhotoImage(file="images\card_back.png")
canvas_img=canvas.create_image(400,275,image=front_img)


title=canvas.create_text(380,150,text="Title",font=(FONT_NAME,35,"bold"))
word=canvas.create_text(380,300,text="Word",font=(FONT_NAME,45,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
random_word_selection()

my_image = tkinter.PhotoImage(file="images/right.png")
rightbutton =tkinter.Button(image=my_image, highlightthickness=0,command=remove_known_word)
rightbutton.grid(row=1,column=0)


wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrongbutton =tkinter.Button(image=wrong_image, highlightthickness=0,command=random_word_selection)
wrongbutton.grid(row=1,column=1)


window.mainloop()
