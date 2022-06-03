from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizinterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.question = "No question yet"
        self.score = 0
        self.quiz = quiz_brain
        # making a window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # import images
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        # score label
        self.score_label = Label(text=f"Score: {self.score}", background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)
        # white text canvas
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text=self.question, fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # buttons
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        # get next question
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
