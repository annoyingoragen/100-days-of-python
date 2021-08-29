import tkinter
window=tkinter.Tk()
window.minsize(width=500,height=500)

label=tkinter.Label()
label['text']="blah"
label.config(padx=20,pady=20)
label.grid(column=0,row=0)


button=tkinter.Button()
button['text']="click"
button.config(padx=20,pady=20)
button.grid(column=1,row=1)

button2=tkinter.Button()
button2['text']="click2"
button2.config(padx=20,pady=20)
button2.grid(column=2,row=0)


input=tkinter.Entry()
input.insert(tkinter.END,string="Entry")
input.grid(column=3,row=2)


window.mainloop()

