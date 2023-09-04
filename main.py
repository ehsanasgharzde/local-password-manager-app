# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '(', ')', '*', '+', '-', '_']
DARKBLUE = "#001E6C"
BLUE = "#035397"
LIGHTBLUE = "#5089C6"
GRAY = '#787A91'
WHITE = '#F9F9F9'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwordgenerator():
    passwordinput.delete(0, END)
    
    letterlist = [choice(LETTERS) for char in range(randint(8, 10))]
    numberlist = [choice(NUMBERS) for char in range(randint(2, 4))]
    symbollist =[choice(SYMBOLS) for char in range(randint(2, 4))]

    charlist = letterlist + numberlist + symbollist
    shuffle(charlist)
    
    password = ''.join(charlist)

    passwordinput.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websitedata = websiteinput.get().title()
    usernamedata = usernameinput.get()
    passworddata = passwordinput.get()

    if len(websitedata) != 0 and len(usernamedata) != 0 and len(passworddata) != 0:

        confirm = messagebox.askokcancel(title=websitedata, message=f'These are the entered details: \nUsername/e-mail: {usernamedata} '
                                                                    f'\nPassword: {passworddata} \nDo you confirm?')
        if confirm:
            with open('PasswordLog.txt', 'a') as file:
                file.write(f'{websitedata} | {usernamedata} | {passworddata}\n')

                websiteinput.delete(0, END)
                passwordinput.delete(0, END)

    else:
        messagebox.showerror(title='Error: Empty Fields!', message='Please fill in all fildes.')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(360, 640)
window.config(bg=LIGHTBLUE)

canvas = Canvas(width=256, height=256, highlightthickness=0, bg=LIGHTBLUE)
image = PhotoImage(file='locklogo.png')
canvas.create_image(128, 128, image=image)
canvas.place(x=128, y=50)

website = Label(text='Website:', highlightthickness=0, bg=LIGHTBLUE)
website.place(x=25, y=340)

username = Label (text='Username/e-mail:', highlightthickness=0, bg=LIGHTBLUE)
username.place(x=25, y=370)

password = Label (text='Password:', highlightthickness=0, bg=LIGHTBLUE)
password.place(x=25, y=400)

passgenerator = Button(text='Generate Password', highlightthickness=0, bg=LIGHTBLUE, activebackground=BLUE, command=passwordgenerator)
passgenerator.place(x=370, y=398)

addbutton = Button(text='Add', highlightthickness=0, width=48, bg=LIGHTBLUE, activebackground=BLUE, command=save)
addbutton.place(x=135, y=430)

websiteinput = Entry(width=56, bg=GRAY)
websiteinput.place(x=135, y=340)
websiteinput.focus()

usernameinput = Entry(width=56, bg=GRAY)
usernameinput.place(x=135, y=370)
usernameinput.insert(0, 'ehsn.asg@gamil.com')

passwordinput = Entry(width=37, bg=GRAY)
passwordinput.place(x=135, y=400)

window.mainloop()