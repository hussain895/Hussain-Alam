import tkinter as tk
from tkinter import messagebox
import re

# ------Login System -------
Sign_In = {
    "Admin": {
        "admin": "admin123"
    },
    "User Name": {
        "user": "user123"
    },
    "Password": {
        "pass": "pass123"
    }
}
def Login():
    try:
        username = username_entry.get()
        password = password_entry.get()
        
        if username in Sign_In["User Name"] and password == Sign_In["User Name"][username]:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        root.focus_set()
        login_button.config(command=Login)
#------GUI Setup for Login -------
root = tk.Tk()
root.title("Login System")
root.geometry("400x400")
root.config(bg="#fff6f6")

#-------Frame for Login -------
login_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
login_frame.pack(pady=30)   
tk.Label(login_frame, text="Username:", bg="#f4f4f4").grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)    
tk.Label(login_frame, text="Password:", bg="#f3e8e8").grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)    

#-------Login Button -------
login_button = tk.Button(login_frame, text="Login", bg="#4da6ff", fg="white", font=("Arial", 12, "bold"))
login_button.grid(row=2, columnspan=2, pady=10)
root.mainloop()



