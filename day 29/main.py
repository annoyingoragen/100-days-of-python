import tkinter
from tkinter import messagebox
import random
import pyperclip

#***************Password generator *******************************

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters=[random.choice(letters) for _ in range(nr_letters)]

    password_symbols=[random.choice(numbers) for _ in range(nr_symbols)]

    password_numbers=[random.choice(symbols) for _ in range(nr_numbers)]

    password_list=password_numbers+password_letters+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    passwordinput.insert(0,password)

    pyperclip.copy(password)
#*******************SAVING DATA IN FILE***************************
def saving():
    website=Websiteinput.get()
    password=passwordinput.get()
    if len(password)==0 or len(website)==0:
        messagebox.showinfo(title="oops",message="Fill all the fields")
        return
    with open("passworddata.txt",mode="a") as datafile:
        passwordandwebsite=Websiteinput.get()+" | "+emailuserinput.get()+" | "+passwordinput.get()+"\n"
        is_okay=messagebox.askokcancel(title="confirmation",message="Do you want to proceed?")
        if is_okay:
         datafile.write(passwordandwebsite)
        else:
            return
    Websiteinput.delete(0,tkinter.END)
    passwordinput.delete(0,tkinter.END)







window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas=tkinter.Canvas(width=200,height=200)
img=tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1, row=0)

Websitelabel=tkinter.Label(text="Website:")
Websitelabel.grid(column=0,row=1)


Websiteinput=tkinter.Entry(width=35)
Websiteinput.grid(column=1,row=1,columnspan=2)
Websiteinput.focus()


emailuserlabel=tkinter.Label(text="Email/Username:")
emailuserlabel.grid(column=0,row=2)

emailuserinput=tkinter.Entry(width=35)
emailuserinput.grid(column=1,row=2,columnspan=2)
emailuserinput.insert(tkinter.END,string="bibliophilemuffie@gmail.com")


passwordlabel=tkinter.Label(text="Password:")
passwordlabel.grid(column=0,row=3)

passwordinput=tkinter.Entry(width=17)
passwordinput.grid(column=1,row=3)

generatepassbutton=tkinter.Button(text="Generate Password",command=generate_password)
generatepassbutton.grid(column=2,row=3)

addpassbutton=tkinter.Button(text="Add",width=30, command=saving)
addpassbutton.grid(column=1,row=4,columnspan=2)


window.mainloop()