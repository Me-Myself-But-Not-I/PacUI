#! /usr/bin/python
import tkinter as tk
import subprocess


Background = "#17a9d6"
Text_Color = "white"
Button_Color = "#0d7a9e"

root = tk.Tk()
pkg = tk.StringVar()

root.title("PacGUI")
root.configure(background=Background)
root.minsize(400, 350)

def install():
    if pkg.get():
        subprocess.run(["sudo", "pacman", "-S", pkg.get()])

def uninstall():
    if pkg.get():
        subprocess.run(["sudo", "pacman", "-Rs", pkg.get()])

def query():
    subprocess.run(["pacman", "-Q"])

def querySpecific():
    if pkg.get():
        res = subprocess.run(["pacman", "-Qi", pkg.get()], capture_output=True, text=True)
        result_label.config(text=res.stdout)
    else:
        result_label.config(text="Please enter a package name first")

def update_selected(*args):
    if pkg.get():
        selected.config(text=f"Selected: {pkg.get()}")
    else:
        selected.config(text="No package selected")

# Main frame with padding
main_frame = tk.Frame(root, background=Background, padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

# Title label
label1 = tk.Label(main_frame, text="PacGUI", font=("Arial", 16, "bold"), 
                  background=Background, foreground=Text_Color)
label1.pack(pady=(0, 5))

# Subtitle label
label2 = tk.Label(main_frame, text="Graphical interface for pacman", font=("Arial", 10),
                  background=Background, foreground=Text_Color)
label2.pack(pady=(0, 15))

# Instruction label
instruction = tk.Label(main_frame, text="Enter package name below:", font=("Arial", 9),
                       background=Background, foreground=Text_Color)
instruction.pack(pady=(0, 5))

# Text entry
text_box = tk.Entry(main_frame, textvariable=pkg, font=("Arial", 11), width=30)
text_box.pack(pady=(0, 10))

# Selected package label
selected = tk.Label(main_frame, text="No package selected", font=("Arial", 9, "italic"),
                    background=Background, foreground=Text_Color)
selected.pack(pady=(0, 15))

# Button frame
button_frame = tk.Frame(main_frame, background=Background)
button_frame.pack(pady=10)

# Install button
Install = tk.Button(button_frame, height=2, width=12, text="Install", 
                    command=install, bg=Button_Color, fg="white", 
                    font=("Arial", 10, "bold"), relief="raised")
Install.pack(pady=5)

# Uninstall button
Uninstall = tk.Button(button_frame, height=2, width=12, text="Uninstall", 
                      command=uninstall, bg=Button_Color, fg="white",
                      font=("Arial", 10, "bold"), relief="raised")
Uninstall.pack(pady=5)

# Query button
Query = tk.Button(button_frame, height=2, width=12, text="List Packages", 
                  command=query, bg=Button_Color, fg="white",
                  font=("Arial", 10, "bold"), relief="raised")
Query.pack(pady=5)

# Query specific button
QuerySpecific = tk.Button(button_frame, height=2, width=20, text="Package Info", 
                          command=querySpecific, bg=Button_Color, fg="white",
                          font=("Arial", 10, "bold"), relief="raised")
QuerySpecific.pack(pady=5)

# Result label for querySpecific
result_label = tk.Label(main_frame, text="", font=("Arial", 9), 
                        background=Background, foreground=Text_Color, 
                        wraplength=350, justify="left")
result_label.pack(pady=(15, 0))

# Update selected label when text changes
pkg.trace_add("write", update_selected)

root.mainloop()
