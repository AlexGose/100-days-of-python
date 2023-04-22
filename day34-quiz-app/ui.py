import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = tkinter.Label(text="Score: 0",
                                         background=THEME_COLOR,
                                         foreground="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Text goes here",
                                                     fill=THEME_COLOR,
                                                     font=('Ariel', 20, 'italic'))

        checkmark_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=checkmark_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        x_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=x_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
