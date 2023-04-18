import pandas as pd
import tkinter
BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    canvas.itemconfig(front_top_text, text="French")
    canvas.itemconfig(front_bottom_text, text=data['French'].sample().iloc[0])


if __name__ == "__main__":
    data = pd.read_csv("data/french_words.csv")
    window = tkinter.Tk()
    window.title("Flashy")
    window.configure(padx=50, pady=50, background=BACKGROUND_COLOR)

    canvas = tkinter.Canvas(height=526, width=800, background=BACKGROUND_COLOR,
                            highlightthickness=0)
    canvas.configure()

    card_front_img = tkinter.PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=card_front_img)
    front_top_text = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'))
    front_bottom_text = canvas.create_text(400, 253, font=('Ariel', 60, "bold"))

    canvas.grid(row=0, column=0, columnspan=2)

    wrong_img = tkinter.PhotoImage(file="images/wrong.png")
    wrong_button = tkinter.Button(image=wrong_img, background=BACKGROUND_COLOR,
                                  highlightthickness=0, command=next_card)
    wrong_button.grid(row=1, column=0)

    right_img = tkinter.PhotoImage(file="images/right.png")
    right_button = tkinter.Button(image=right_img, background=BACKGROUND_COLOR,
                                  highlightthickness=0, command=next_card)
    right_button.grid(row=1, column=1)

    next_card()

    window.mainloop()
