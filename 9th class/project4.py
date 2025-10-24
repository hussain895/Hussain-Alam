import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Window Calculator")

# Entry widget to display calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    action = lambda x=button: click_button(x) if x not in ['=', 'C'] else None
    btn = tk.Button(root, text=button, width=4, height=2, font=('Arial', 20))
    
    if button == 'C':
        btn.config(command=clear, fg='red')
    elif button == '=':
        btn.config(command=calculate, fg='green')
    else:
        btn.config(command=action)
    
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
