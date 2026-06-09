#! /usr/bin/python
import tkinter as tk
import subprocess

Background = "#17a9d6"

root = tk.Tk()
pkg = ""

root.title("PacGUI")
root.configure(background = Background)
root.minsize(350, 200)

label1 = tk.Label(root, text="PacGUI, your graphical interface to use pacman")
label1.pack()

label2 = tk.Label(root, text="Type a package name below, in lowercase(not mandatory for package list)")
label2.pack()

pkg = tk.StringVar()
text_box = tk.Entry(root, textvariable=pkg, )
text_box.pack()

if pkg != "":
    sel = pkg.get()
else:
    sel = "none selected"

selected = tk.Label(root, text=sel)
selected.pack()

Install = tk.Button(root, height=1, width=15, text = "Install", command="install()")
Install.pack()

Uninstall = tk.Button(root, height=1, width=15, text = "Uninstall", command="uninstall()")
Uninstall.pack()

Query = tk.Button(root, height=1, width=15, text = "List all packages", command="query()")
Query.pack()

QuerySpecific = tk.Button(root, height=1, width=15, text = "get info on specified package", command="querySpecific()")
QuerySpecific.pack()

def changeText():
    selected(text=pkg)
def install():
    if pkg != "":
        subprocess.run(args="sudo pacman -S " + pkg.get())
def uninstall():
    if pkg != "":
        subprocess.run(args="sudo pacman -Rs " + pkg.get())
def query():
    subprocess.run(args="pacman -Q")
def querySpecific():
    res = subprocess.run(args="pacman -Qi" + pkg.get(),capture_output=True, text=True)
    Res = tk.Label(text=res)
    Res.pack()


root.mainloop()
