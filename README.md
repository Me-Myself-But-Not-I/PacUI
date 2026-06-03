# PacUI
A TUI for  using debian's APT and arch's pacman package managers.

## Installation guide
PacUI, in it's current state, is just a single .py file. 
To install and use PacUI, there are 3 steps.
1. Install the script, this can be either:
   a. Install the PacUI.py file(or APTUI.py for debian)
   b. Create a new text file, copy the code into it, then save it as "PacUI.py" or "APTUI.py", I would recommend putting this in your home directory(~/...)
2. Build the file, run the command "chmod +x /home/<user name>/Downloads/PacUI.py"(or the location the file is currently in)
3. Run the program, by typing, in the terminal "./PacUI.py" or "./APTUI.py"

## Features
In it's current, work in progress, state, PacUI is just a guided CLI for pacman. It does not have every command in pacman accessible, nor is planned to.
Currently, PacUI is able to:
- Install packages, through pacman
- Query packages, through pacman
- List installed packages, through pacman
- Update packages, through pacman
- Give you an error message when you make a typo

## Required Dependencies
PacUI requires that python is installed. PacUI was made with python 3.14, it is recommeded to use the latest version of python at the time of use.

## How it works
PacUI is a simple script, it gives a prompt, you press a letter then enter, then it will run a command for you. 

## Planned updates
The main thing to be added is a proper GUI using tkinter.
