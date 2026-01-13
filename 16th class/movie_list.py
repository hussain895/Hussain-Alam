import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
movie = []
list = int(input("How Many Movies Do you Want To Add : "))

for i in range(list):
    movie_list = input(f"Enter The Movie {i+1} : ")
    movie.append(movie_list)

print("\n Current Movie List : " , movie)


movie.sort()
print("\n Sorted Movie List : " , movie)

movie_name = input("Enter A Movie To Check How Many Times It Repeated : ")
count = movie.count(movie_name)
print(f"\n {movie_name} Repeated {count} Times")

letter_groups = {}   

for m in movie:
    first_letter = m[0].upper()
    if first_letter not in letter_groups:
        letter_groups[first_letter] = []
    letter_groups[first_letter].append(m)


for letter, movie_list in letter_groups.items():
    print(f"\n{letter} → {len(movie_list)} movie(s)")
    for mov in movie_list:
        print("   -", mov)

remove_movie = input("\nEnter a Movie to Remove: ")
if remove_movie in movie:
    movie.remove(remove_movie)
    print(f"\n'{remove_movie}' removed successfully.")
else:
    print(f"\n'{remove_movie}' not found in the list.")

print("\nFinal Movie List:", movie)

root = tk.Tk()
root.title("Movie Manager GUI")
root.geometry("400x400")
movie_listbox = tk.Listbox(root, width=50, height=15)
movie_listbox.pack(pady=20)
for m in movie:
    movie_listbox.insert(tk.END, m)
def remove_selected_movie():
    selected_movie = movie_listbox.get(tk.ACTIVE)
    if selected_movie in movie:
        movie.remove(selected_movie)
        movie_listbox.delete(tk.ACTIVE)
        messagebox.showinfo("Success", f"'{selected_movie}' removed successfully.")
    else:
        messagebox.showerror("Error", f"'{selected_movie}' not found in the list.")
remove_button = tk.Button(root, text="Remove Selected Movie", command=remove_selected_movie)
remove_button.pack(pady=10)
update_button = tk.Button(root, text="Update Movie List", command=lambda: movie_listbox.delete(0, tk.END) or [movie_listbox.insert(tk.END, m) for m in movie])
update_button.pack(pady=10)
update_display = tk.Button(root, text="Display Movie List", command=lambda: messagebox.showinfo("Movie List", "\n".join(movie)))
update_display.pack(pady=10)
update_display()
root.mainloop()











