# try:
#     with open("a_file.txt") as file:
#         print("file opened")
#         a_dictionary={"key":"value"}
#         print(a_dictionary["jsdkfb"])
# except FileNotFoundError:
#     with open("a_file.txt","w") as file:
#         file.write("something")
# except KeyError as errormessaeg:
#     print(f"That key does {errormessaeg} not exist")



"""

Performing exercise

"""
# import pandas
#
# natodataframe=pandas.read_csv("nato_phonetic_alphabet.csv")
#
# nato_dict={rowframe.letter : rowframe.code for (index,rowframe) in natodataframe.iterrows()}
#
# word=input("Enter a word: ").upper()
# try:
#     phonetic_list=[ nato_dict[letter] for letter in word ]
# except KeyError :
#     print("Sorry only letters in the alphabet please")
# else:
#     print(phonetic_list)


import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

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
    email=emailuserinput.get()

    if len(password)==0 or len(website)==0:
        messagebox.showinfo(title="oops",message="Fill all the fields")
        return

    passwordandwebsite = {
        website: {
            "email": email,
            "password": password}

    }

    # Reading old data from file
    try:
        with open("passworddata.json",mode="r")as datafile:
            datafromfile=json.load(datafile)
    except FileNotFoundError:
        with open("passworddata.json",mode="w") as datafile:
            json.dump(passwordandwebsite,datafile)
    else:
        # Updating the data
        datafromfile.update(passwordandwebsite)
        #saving updated data
        with open("passworddata.json",mode="w") as datafile:

            is_okay=messagebox.askokcancel(title="confirmation",message="Do you want to proceed?")
            if is_okay:
                 json.dump(datafromfile,datafile,indent=4)
            else:
                return
    finally:
        Websiteinput.delete(0,tkinter.END)
        passwordinput.delete(0,tkinter.END)

#*************************************SEARCHING*****************************
def search_password_for_website():
    website = Websiteinput.get()
    try:
        with open("passworddata.json",mode="r") as datafile:
            data_from_file=json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="No data file found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="ERROR", message="No data found in file")
    else:
        if website in data_from_file:
            email=data_from_file[website]['email']
            password=data_from_file[website]['password']
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message="No details for this website")







window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas=tkinter.Canvas(width=200,height=200)
img=tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1, row=0)

Websitelabel=tkinter.Label(text="Website:")
Websitelabel.grid(column=0,row=1)


Websiteinput=tkinter.Entry(width=23)
Websiteinput.grid(column=1,row=1,padx=12,sticky='e')
Websiteinput.focus()

searchbutton=tkinter.Button(text="Search",width=15,command=search_password_for_website)
searchbutton.grid(row=1,column=2)


emailuserlabel=tkinter.Label(text="Email/Username:")
emailuserlabel.grid(column=0,row=2)

emailuserinput=tkinter.Entry(width=35)
emailuserinput.grid(column=1,row=2,columnspan=2)
emailuserinput.insert(tkinter.END,string="bibliophilemuffie@gmail.com")


passwordlabel=tkinter.Label(text="Password:")
passwordlabel.grid(column=0,row=3)

passwordinput=tkinter.Entry(width=23)
passwordinput.grid(column=1,row=3,padx=12,sticky='e')

generatepassbutton=tkinter.Button(text="Generate Password",command=generate_password)
generatepassbutton.grid(column=2,row=3)

addpassbutton=tkinter.Button(text="Add",width=30, command=saving)
addpassbutton.grid(column=1,row=4,columnspan=2)


window.mainloop()