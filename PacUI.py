#! /usr/bin/python
import os

service = ""

print("Welcome to PacUI")
print("Your prompt based, guided interface for Arch Linux's Pacman package manager.")
print("All inputs are case-sensitive, please type exactly as written in the prompt.")
explanation = input("Please press Y followed by enter to display all commands used, or press enter to ignore this. ")
service = input("press Q followed by enter to list installed packages, QD to get details on a specific package, I to install a package, R to delete a package, or U to update all packages: ")
if service == "Q":
    if explanation == "Y":
        print("Command run is: pacman -Q")
    os.system("pacman -Q")
elif service == "QD":
    if explanation == "Y":
        print("Command run is: pacman -Qi <package>")
    QueryTarget = input("Type package name here: ")
    os.system("pacman -Qi " + QueryTarget)
elif service == "I":
    IMode = input("Press P for arch packages or A for AUR packages: ")
    if IMode == "P":
        if explanation == "Y":
            print("Command run is: sudo pacman -S <package>")
        package = input("Type the name of your desired package here(if you want multiple packages, seperate with a space): ")
        print("To confirm, you are installing " + package)
        input("Press enter to install " + package)
        os.system("sudo -S pacman -S " + package)
    elif IMode == "S":
        if explanation == "Y":
            print("Command run is: yay -S <package>")
        package = input("Type the name of your desired package here(if you want multiple packages, seperate with a space): ")
        print("To confirm, you are installing " + package)
        input("Press enter to install " + package)
        os.system("yay -S " + package)
elif service == "R":
    mode = input("Press A for advanced mode, or S for easy ")
    if mode == "S":
        if explanation == "Y":
            print("Command run is: sudo pacman -Rs <package>")
        packageDel = input("Type the name of your desired package here(if you want multiple packages, seperate with a space): ")
        print("To confirm, you are deleting " + packageDel)
        input("Press enter to delete " + packageDel)
        os.system("sudo -S pacman -Rs " + packageDel)
    elif mode ==  "A":
        deleteA = input("Press R to delete a package, D to delete a package and all it's dependencies, F to force delete a package and all it's dependencies: ")
        if deleteA == "R":
            if explanation == "Y":
                print("Command run is: sudo pacman -R <package>")
            packageDel = input("Type the name of your desired package here(if you want multiple packages, seperate with a space): ")
            print("To confirm, you are deleting " + packageDel)
            input("Press enter to delete " + packageDel)
            os.system("sudo -S pacman -R " + packageDel)
        if deleteA == "D":
            if explanation == "Y":
                print("Command run is: sudo pacman -Rs <package>")
            packageDel = input("Type the name of your desired package here(if you want multiple packages, seperate with a space): ")
            print("To confirm, you are deleting " + packageDel)
            input("Press enter to delete " + packageDel)
            os.system("sudo -S pacman -Rs " + packageDel)
        if deleteA == "F":
            print("WARNING, this process will delete a package regardless of use, this is capable of causing major system damage")
            if explanation == "Y":
                print("Command run is: sudo pacman -Rns -dd <package>")
            packageDel = input("Type the name of your desired package here(if you want multiple packages, seperate with a space): ")
            print("To confirm, you are deleting " + packageDel)
            input("Press enter to delete " + packageDel)
            os.system("sudo -S pacman -Rns -dd " + packageDel)
    else:
        print("Error: invalid selection")
elif service == "U":
    if explanation == "Y":
        print("Command run is: sudo pacman -Syu")
    UDecision = input("Are you sure you would like to update (Y/N)")
    if UDecision == "Y":
        os.system("sudo -S pacman -Syu")
    else:
        print("Update cancelled")
        os.system("./PacUI.py")
else:
    print("Error: invalid selection")
    errorOption = input("Press I for some possible causes and potential fixes")
    if errorOption == "I":
        print("Your use of PacUI encountered an issue. There are many reasons this could happen, and ways to fix it")
        print("The first possible cause is incorrect capitalisation, this is your fault, and most likely")
        print("PacUI requires that all input prompts are capitalised, unless specified otherwise, please retry, ensuring all inputs are capitalised")
        print("The second possibility is just, simply, an unknown error")
        print("In this case you can try:")
        print("   A. Restart PacUI, then try again")
        print("   B. Reinstall PacUI then try again")
        print("   C. try your command with pacman in the terminal")
        print("   D. Reinstall/update python(in terminal, run sudo pacman -Syu python)")
        print("   E. Install Debian")
    elif errorOption != "":
        print("You selected an invalid option. Remember: selections must be capitalised, and packages must be lowercase.")
    else:
        pass
if "Y" == input("Press Y then enter to continue package management"):
    os.system("./PacUI.py")
