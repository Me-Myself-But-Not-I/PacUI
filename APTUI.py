#! /usr/bin/python
import os

print("Please press I to install a package; R to uninstall a package; Q to list installed packages;")
print("QD to get details about a specific package; U to update a packages; UA to update all packages; or H for more details, followed by enter.")
print("Your selection should be capitalised, package names should be lowercase, and confirmation(y/n) should be lowercase")
selec = input()

advanced = input("Would you like to be told what commands are being run? (y/n)")

if selec == "I":
    pkg = input("Type the package name here: ")
    if advanced == "y":
        print("sudo apt install " + pkg)
    if "y" == input("Are you sure you would like to install "+ pkg +"?(y/n)"):
        os.system("sudo apt install " + pkg)
elif selec == "R":
    pkg = input("Type the package name here: ")
    if advanced == "y":
        print("sudo apt remove " + pkg)
    if "y" == input("Are you sure you would like to uninstall " + pkg + "?(y/n)"):
        os.system("sudo apt remove " + pkg)
elif selec == "Q":
    if advanced == "y":
        print("apt list --installed")
    os.system("apt list --installed")
elif selec == "QD":
    pkg = input("Type the package name here: ")
    if advanced == "y":
        print("sudo apt show " + pkg)
    os.system("sudo apt show " + pkg)
elif selec == "U":
    pkg = input("Type the package name here: ")
    if advanced == "y":
        print("sudo apt upgrade " + pkg)
    os.system("sudo apt upgrade " + pkg)
elif selec == "UA":
    if advanced == "y":
        print("sudo apt full-upgrade")
    print("are you sure?(y/n)")
    if "y" == input():
        os.system("sudo apt full-upgrade")
elif selec == "H":
    print("This is APTUI")
    print("A prompt-based system for using the APT package manager.")
    print("To see prompt options, view the starting message above.")
    print("If you have had an error check these things first:")
    print("  A. Your selection(I to install, R to remove, etc) is capitalised.")
    print("  B. Your package name is lowercase.")
    print("  C. You're connected to the internet")
    print("If it still fails, try:")
    print("  A. Reload APTUI.")
    print("  B. Reinstall APTUI")
    print("  C. Reinstall python.")
    print("  D. Run the command to do what you require with apt in the terminal.")
    print("  E. Install RedHat")
else:
    print("Error: Invalid selection.")
    print("Ensure your selection is capitalised, or choose H for help")
if "y" == input("press y to restart "):
    if advanced == "y":
        print("./APTUI.py")
    os.system("./APTUI.py")
