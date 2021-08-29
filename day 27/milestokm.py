import tkinter

def milestokm():
    miles=int(input.get())
    label3['text']=miles*1.609

window=tkinter.Tk()
window.minsize(width=200,height=60)
window.config(padx=10,pady=10)

input=tkinter.Entry(width=10)
input.grid(column=1,row=0)

label1=tkinter.Label()
label1['text']="Miles"
label1.grid(column=2,row=0)

label2=tkinter.Label()
label2['text']="is equal to"
label2.grid(column=0,row=1)

label3=tkinter.Label(width=10)
label3['text']=" "
label3.grid(column=1,row=1)

label4=tkinter.Label()
label4['text']="Km"
label4.grid(column=2,row=1)

button=tkinter.Button(command=milestokm)
button['text']="Calculate"
button.grid(column=1,row=2)



window.mainloop()