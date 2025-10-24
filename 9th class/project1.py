
def mad_libs():
    print("Let's play Mad Libs!")
    
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    
    story = f"Yesterday, I went to the {place}. It was very {adjective}! " \
            f"I saw a {noun} there, and it {verb} right in front of me!"
    
    print("\nHere's your story:")
    print(story)

if __name__ == "__main__":
    mad_libs()



import tkinter as tk
from tkinter import messagebox

class MadLibsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mad Libs Game")
        self.root.geometry("400x400")

        # Instructions label
        self.label = tk.Label(root, text="Fill in the blanks and press 'Generate Story'!", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entry labels and fields
        self.entries = {}
        prompts = ["Adjective", "Noun", "Verb (past tense)", "Adverb", "Adjective", "Noun"]

        for prompt in prompts:
            frame = tk.Frame(root)
            frame.pack(pady=5)
            lbl = tk.Label(frame, text=prompt + ": ", width=15, anchor='w')
            lbl.pack(side=tk.LEFT)
            ent = tk.Entry(frame, width=25)
            ent.pack(side=tk.LEFT)
            self.entries[prompt] = ent

        # Button to generate story
        self.button = tk.Button(root, text="Generate Story", command=self.generate_story)
        self.button.pack(pady=20)

        # Text box for the story output
        self.story_text = tk.Text(root, height=8, width=50, wrap='word')
        self.story_text.pack(pady=10)

    def generate_story(self):
        # Get input values
        try:
            adj1 = self.entries["Adjective"].get()
            noun1 = self.entries["Noun"].get()
            verb_past = self.entries["Verb (past tense)"].get()
            adverb = self.entries["Adverb"].get()
            adj2 = self.entries["Adjective"].get()  # Using same prompt twice for simplicity
            noun2 = self.entries["Noun"].get()      # Using same prompt twice for simplicity

            # Check all fields filled
            for val in [adj1, noun1, verb_past, adverb, adj2, noun2]:
                if not val.strip():
                    messagebox.showwarning("Input Error", "Please fill in all fields.")
                    return

            # Create the story
            story = (
                f"Today I went to the zoo and saw a {adj1} {noun1}. "
                f"It {verb_past} {adverb} past me. "
                f"I was so {adj2} that I couldn't believe my {noun2}!"
            )

            # Display the story
            self.story_text.delete(1.0, tk.END)
            self.story_text.insert(tk.END, story)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MadLibsGame(root)
    root.mainloop()
