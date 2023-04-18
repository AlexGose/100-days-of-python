import tkinter
BACKGROUND_COLOR = "#B1DDC6"


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Flashy")
    window.configure(padx=50, pady=50, background=BACKGROUND_COLOR)

    canvas = tkinter.Canvas(height=526, width=800, background=BACKGROUND_COLOR,
                            highlightthickness=0)
    canvas.configure()

    logo_img = tkinter.PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=logo_img)
    canvas.grid(row=0, column=0, columnspan=2)

    wrong_img = tkinter.PhotoImage(file="images/wrong.png")
    wrong_button = tkinter.Button(image=wrong_img, background=BACKGROUND_COLOR,
                                  highlightthickness=0)
    wrong_button.grid(row=1, column=0)

    right_img = tkinter.PhotoImage(file="images/right.png")
    right_button = tkinter.Button(image=right_img, background=BACKGROUND_COLOR,
                                  highlightthickness=0)
    right_button.grid(row=1, column=1)

    window.mainloop()
