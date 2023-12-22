# ------------------------------------------------------
# Password generator
# ------------------------------------------------------
'''
- for creating passwords and saving them into a TXT file
- user has to fill in the website name, email or username and password
- the password can be generated randomly from letters, numbers and symbols
- all inputs are saved as a new line in a file
'''
# ------------------------------------------------------

# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ------------------------------------------------------

# ------------------------------------------------------
# Define constants
# ------------------------------------------------------
FONT_NAME = "Courier"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ------------------------------------------------------


# ------------------------------------------------------
# Define functions
# ------------------------------------------------------
# PASSWORD GENERATOR
def generate_passw():
    """Randomly generate password from letters, numbers and symbols."""
    # randomly create part of the passw (from letters, symbols and numbers)
    password_letters = [random.choice(LETTERS) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(SYMBOLS) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(NUMBERS) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # join all randomly generated letters, symbols and numbers into one variable
    generated_password = "".join(password_list)

    # insert the passw into the entry
    entry_passw.delete(0, END)
    entry_passw.insert(0, generated_password)

    # copy the passw to the clipboard for immediate use
    # pyperclip.copy(generated_password)


# SAVE PASSWORD
def clear_data():
    """Clear inserted text in website and password entry."""
    entry_website.delete(0, END)
    entry_passw.delete(0, END)


def save_passw():
    """Save inputs of website, email and password into a file."""
    website = entry_website.get()
    email = entry_email.get()
    password = entry_passw.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please, do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \n "
                                                              f"\nIs it OK to save it?")
        if is_ok:
            with open("data_passw.txt", mode="a") as file_passw:
                file_passw.write(f"{website} | {email} | {password} \n")
            clear_data()
# ------------------------------------------------------


# ------------------------------------------------------
# GUI
# ------------------------------------------------------
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
label_website = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
label_email.grid(row=2, column=0)
label_passw = Label(text="Password:", font=(FONT_NAME, 12, "bold"))
label_passw.grid(row=3, column=0)

# Button
button_add = Button(text="Add", width=42, font=(FONT_NAME, 10, "bold"), command=save_passw)
button_add.grid(row=4, column=1, columnspan=2)
button_generate = Button(text="Generate password", font=(FONT_NAME, 10, "bold"), command=generate_passw)
button_generate.grid(row=3, column=2)

# Entry
entry_website = Entry(width=44)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=44)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "username@gmail.com")
entry_passw = Entry(width=24)
entry_passw.grid(row=3, column=1)

# Mainloop
window.mainloop()
# ------------------------------------------------------
