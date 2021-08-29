import tkinter

window=tkinter.Tk()
window.title("name of the window")
window.minsize(width=500, height=500)

#LABEL TEXT IN WINDOW
label_in_window=tkinter.Label(text="yada yada",font=("Arial",24,"bold"))
label_in_window.pack()

def button_clicked():
    """action is performed when button gets clicked"""
    label_in_window["text"]=input.get()

#BUTTON  IN WINDOW
button_in_window=tkinter.Button(text="Get Text from input field",command=button_clicked)
button_in_window.pack()



#INPUT FIELD IN WINDOW
input=tkinter.Entry(width=30)
input.insert(tkinter.END, string="abc@gmail.com")
input.pack()

window.mainloop()

