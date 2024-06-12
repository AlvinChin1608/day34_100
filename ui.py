from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): # the quiz_brain: DataType
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Open Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column= 1)

        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, width=280, text="Text Here", fill="black", font=("Arial", 19, "italic"))
        self.canvas.grid(row= 1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/15")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="The End")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="light green")
        else:
            self.canvas.config(bg="pink")
        self.window.after(200, self.get_next_question)