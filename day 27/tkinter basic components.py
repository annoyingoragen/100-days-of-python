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

#TEXTBOX in window
textbox=tkinter.Text(height=5,width=30)
textbox.focus()
textbox.insert(tkinter.END,"Enter information here")
textbox.pack()


#SPINBOX in window
spinbox_label=tkinter.Label()
def spinbox_used():
    spinbox_label['text']=spinbox.get()
    spinbox_label.pack()
spinbox=tkinter.Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()


#CHECKBOX in window
checkbox_label=tkinter.Label()
def checkbox_used():
    checkbox_label['text']=checked_state.get()
    checkbox_label.pack()

checked_state=tkinter.IntVar()
checkbutton=tkinter.Checkbutton(text="Save Password",variable=checked_state,command=checkbox_used)
checkbutton.pack()


#RADIOBUTTON in window

radiobutton_label=tkinter.Label()
def radiobutton_used():
    radiobutton_label['text']=radio_state.get()
    radiobutton_label.pack()
radio_state=tkinter.IntVar()
radiobutton_1=tkinter.Radiobutton(text="Male",value=1,variable=radio_state,command=radiobutton_used)
radiobutton_2=tkinter.Radiobutton(text="Female",value=2,variable=radio_state,command=radiobutton_used)
radiobutton_1.pack()
radiobutton_2.pack()

#LIST in window
listbox_label=tkinter.Label()
def listbox_used(event):
    listbox_label['text']=listbox.get(listbox.curselection())
    listbox_label.pack()
listbox=tkinter.Listbox()
fruits=["Peach","orange","banana","Cherry"]
for items in fruits:
    listbox.insert(fruits.index(items),items)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()
