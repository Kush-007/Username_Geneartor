#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_username(include_numbers, include_special_chars, length):
    adjectives = ["Cool", "Fast", "Brave", "Happy", "Smart", "Mighty", "Fierce", "Witty", "Lucky"]
    nouns = ["Tiger", "Eagle", "Lion", "Shark", "Dragon", "Falcon", "Wolf", "Panther", "Cheetah"]
    
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    return username[:length]

def save_username(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")
    messagebox.showinfo("Success", f"Username saved to {filename}")

def generate_and_display():
    length = length_slider.get()
    include_numbers = num_var.get()
    include_special_chars = special_var.get()
    
    username = generate_username(include_numbers, include_special_chars, length)
    username_var.set(username)

def save_current_username():
    username = username_var.get()
    if username:
        save_username(username)
    else:
        messagebox.showwarning("Warning", "No username generated yet!")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Random Username Generator")
root.geometry("400x350")
root.configure(bg="#2C2F33")

def style_button(btn):
    btn.config(font=("Arial", 12, "bold"), bg="#7289DA", fg="white", bd=0, relief="flat", padx=10, pady=5)
    btn.bind("<Enter>", lambda e: btn.config(bg="#5865F2"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#7289DA"))

tk.Label(root, text="Generated Username:", font=("Arial", 12, "bold"), fg="white", bg="#2C2F33").pack(pady=5)
username_var = tk.StringVar()
username_entry = tk.Entry(root, textvariable=username_var, font=("Arial", 14), state="readonly", width=25, justify="center", bg="#99AAB5", fg="black", bd=0, relief="flat")
username_entry.pack(pady=5)

num_var = tk.BooleanVar()
special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=num_var, font=("Arial", 10), bg="#2C2F33", fg="white", selectcolor="#23272A", activebackground="#2C2F33").pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Arial", 10), bg="#2C2F33", fg="white", selectcolor="#23272A", activebackground="#2C2F33").pack()

tk.Label(root, text="Username Length:", font=("Arial", 10, "bold"), fg="white", bg="#2C2F33").pack()
length_slider = tk.Scale(root, from_=6, to=15, orient="horizontal", bg="#2C2F33", fg="white", troughcolor="#7289DA", highlightthickness=0)
length_slider.set(8)
length_slider.pack()

generate_btn = tk.Button(root, text="Generate Username", command=generate_and_display)
save_btn = tk.Button(root, text="Save Username", command=save_current_username)
style_button(generate_btn)
style_button(save_btn)

generate_btn.pack(pady=10)
save_btn.pack()

root.mainloop()

