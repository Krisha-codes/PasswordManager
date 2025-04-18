from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols+ password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)== 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title = "Oops", message = "Please make sure you haven't left any fields empty.")
    else:

        is_ok =messagebox.askokcancel(title = website, message = f"These are the details entered: \n"
                                                          f"Email: {email} \n {password}\nIs it ok to save?")
        if is_ok:
            with open("Passwords.txt", "a") as passwords:
               passwords.write(f"{website}  |  {password}  |  {email}\n")
               website_entry.delete(0,END)
               password_entry.delete(0,END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)
image = PhotoImage(file= "logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100, 100, image = image)
canvas.grid(column = 1 , row =0)

web_label = Label(text= "Website:")
email_label = Label(text= "Email/Username:")
password_label= Label(text= "Password:")
pass_generate = Button(text = "Generate Password", command = generate_password)
add_button = Button(text = "Add", width = 36, command= save)

web_label.grid(column =0, row = 1)
email_label.grid(column =0, row = 2)
password_label.grid(column= 0, row= 3)
pass_generate.grid(column= 2, row= 3)
add_button.grid(column = 1, row = 4, columnspan = 2)

website_entry = Entry(width = 35)
website_entry.grid(column = 1, row = 1, columnspan = 2, sticky = "EW")
website_entry.focus()

email_entry = Entry(width = 35)
email_entry.grid(column =1, row= 2, columnspan = 2, sticky = "EW")
email_entry.insert(0, "krishakedia30@gmail.com")

password_entry = Entry(width = 21)
password_entry.grid(column= 1, row = 3, sticky = "EW")

window.mainloop()
