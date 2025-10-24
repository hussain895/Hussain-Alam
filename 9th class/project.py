import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')  # \r makes the timer update in place
        time.sleep(1)
        seconds -= 1
    print("Time's up! ⏰")

if __name__ == "__main__":
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number.")


import tkinter as tk

def start_countdown():
    try:
        # Get input time in seconds
        total_seconds = int(entry.get())
        countdown(total_seconds)
    except ValueError:
        label.config(text="Please enter a valid integer!")

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        label.config(text=time_format)
        # Call this function again after 1 second (1000 milliseconds)
        root.after(1000, countdown, seconds - 1)
    else:
        label.config(text="Time's up!")

# Create main window
root = tk.Tk()
root.title("Countdown Timer")

# Input field for seconds
tk.Label(root, text="Enter time in seconds:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Start button
start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=5)

# Label to show the countdown
label = tk.Label(root, text="00:00", font=("Helvetica", 48))
label.pack(pady=20)

root.mainloop()
