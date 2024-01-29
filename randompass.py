import tkinter as tk
from tkinter import messagebox
import random
import string
import csv

def generate_password(password_var, password_length_var, include_digits_var, include_special_chars_var):
    length = password_length_var.get()
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def save_password(password_var, app_name_var):
    password = password_var.get()
    app_name = app_name_var.get()

    if not password:
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    if not app_name:
        messagebox.showwarning("Warning", "Enter the app or service name.")
        return

    with open("passwords.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([app_name, password])
        messagebox.showinfo("Password Saved", f"Password for {app_name} saved to passwords.csv")

def show_all_passwords():
    try:
        with open("passwords.csv", "r") as file:
            csv_data = file.read()
            if not csv_data:
                messagebox.showinfo("No Passwords", "No passwords saved.")
                return

            # Display passwords in a new window
            passwords_window = tk.Tk()
            passwords_window.title("All Passwords")

            text_widget = tk.Text(passwords_window, height=15, width=40)
            text_widget.pack()

            text_widget.insert(tk.END, csv_data)
            text_widget.config(state='disabled')

            passwords_window.mainloop()

    except FileNotFoundError:
        messagebox.showinfo("No Passwords", "No passwords saved yet.")

def main():
    root = tk.Tk()
    root.title("Password Generator")

    # Variables
    password_var = tk.StringVar()
    app_name_var = tk.StringVar()
    password_length_var = tk.IntVar(value=12)
    include_digits_var = tk.BooleanVar(value=True)
    include_special_chars_var = tk.BooleanVar(value=True)

    # GUI Elements
    tk.Label(root, text="Password Length:").pack(pady=5)
    tk.Scale(root, from_=6, to=30, orient=tk.HORIZONTAL, variable=password_length_var).pack()

    tk.Label(root, text="For App/Service:").pack(pady=5)
    tk.Entry(root, textvariable=app_name_var, width=30).pack()

    tk.Checkbutton(root, text="Include Digits", variable=include_digits_var).pack()
    tk.Checkbutton(root, text="Include Special Characters", variable=include_special_chars_var).pack()

    tk.Button(root, text="Generate Password", command=lambda: generate_password(password_var, password_length_var, include_digits_var, include_special_chars_var)).pack(pady=10)

    tk.Entry(root, textvariable=password_var, state='readonly', width=30).pack(pady=5)

    tk.Button(root, text="Save Password", command=lambda: save_password(password_var, app_name_var)).pack(pady=5)
    tk.Button(root, text="Show All Passwords", command=show_all_passwords).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
