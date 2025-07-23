
import random
import tkinter as tk
from tkinter import messagebox

letters = list('abcdefghijklmnopqrstuvwxyz')
numbers = list('0123456789')
symbols = ['!', '@', '#', '$', '%', '"', "'", '<', '>', ',', '.', '?', '/']

def generate_password():
        try:
                pass_letters = int(entry_letters.get())
                pass_numbers = int(entry_numbers.get())
                pass_symbols = int(entry_symbols.get())
        except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers.")
                return

        # Easy Password
        password = ""
        for _ in range(pass_letters):
                password += random.choice(letters)
        for _ in range(pass_symbols):
                password += random.choice(symbols)
        for _ in range(pass_numbers):
                password += random.choice(numbers)
        easy_password_var.set(password)

        # Strong Password
        password_list = []
        for _ in range(pass_letters):
                password_list.append(random.choice(letters))
        for _ in range(pass_symbols):
                password_list.append(random.choice(symbols))
        for _ in range(pass_numbers):
                password_list.append(random.choice(numbers))
        random.shuffle(password_list)
        strong_password = "".join(password_list)
        strong_password_var.set(strong_password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="How many letters?").grid(row=0, column=0)
entry_letters = tk.Entry(root)
entry_letters.grid(row=0, column=1)

tk.Label(root, text="How many numbers?").grid(row=1, column=0)
entry_numbers = tk.Entry(root)
entry_numbers.grid(row=1, column=1)

tk.Label(root, text="How many symbols?").grid(row=2, column=0)
entry_symbols = tk.Entry(root)
entry_symbols.grid(row=2, column=1)

tk.Button(root, text="Generate Passwords", command=generate_password).grid(row=3, columnspan=2, pady=10)

easy_password_var = tk.StringVar()
strong_password_var = tk.StringVar()

tk.Label(root, text="Easy Password:").grid(row=4, column=0)
tk.Entry(root, textvariable=easy_password_var, width=30).grid(row=4, column=1)

tk.Label(root, text="Strong Password:").grid(row=5, column=0)
tk.Entry(root, textvariable=strong_password_var, width=30).grid(row=5, column=1)

root.mainloop()