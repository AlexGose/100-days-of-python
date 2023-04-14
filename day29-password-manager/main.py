import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as file:
        file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = tkinter.Entry(width=45)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "default@email.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=25)
password_entry.grid(row=3, column=1)

password_button = tkinter.Button(text="Generate Password")
password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
