import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I’m thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()

import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("300x200")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < 1 or guess > 100:
                self.result_label.config(text="Please enter a number between 1 and 100.")
            elif guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.result_label.config(text="You won! Press Reset to play again.")
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
