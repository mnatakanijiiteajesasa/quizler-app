from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOUR = "#375362"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOUR)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOUR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Quiz Text",
            fill=THEME_COLOUR,
            font=("Arial", 10, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_test = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_test)
        else:
            self.canvas.itemconfig(self.question_text, text="You have attempted all quizzes")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.user_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.user_feedback(is_right)

    def user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)







