def quiz():
    score = 0
    print("Welcome to the Quiz!\n")

    # Question 1
    answer1 = input("What is the capital of France? ").strip().lower()
    if answer1 == "paris":
        score += 1

    # Question 2
    answer2 = input("What is 5 + 7? ").strip()
    if answer2 == "12":
        score += 1

    # Question 3
    answer3 = input("What color do you get when you mix red and white? ").strip().lower()
    if answer3 == "pink":
        score += 1

    print(f"\nYour final score is {score} out of 3!")

if __name__ == "__main__":
    quiz()


import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")

        # Sample quiz data: list of dicts with question, options, answer
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "answer": "Mars"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
                "answer": "William Shakespeare"
            },
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.option_buttons = []

        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12))
            rb.pack(anchor='w')
            self.option_buttons.append(rb)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        q = self.questions[self.current_question]
        self.question_label.config(text=q["question"])
        self.var.set(None)  # Clear selection
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def submit_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an answer before submitting.")
            return

        correct_answer = self.questions[self.current_question]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question >= len(self.questions):
            messagebox.showinfo("Quiz Finished", f"Your score is {self.score} out of {len(self.questions)}.")
            self.root.destroy()  # Close the window after finishing
        else:
            self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
