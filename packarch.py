# Created by Tom5521 or Angel
# Under the GPL license 3.0

from os import getcwd, chdir
from os import system as sys
from time import sleep as sl

current_directoy = getcwd()

hide = [">/dev/null 2>&1", "|ls > .out && rm -rf .out", "clear"]
sp = " "
All_text_cond = True
words = [
    "Installing ",  # 0
    "Installed",  # 1
    "Update Complete",  # 2
    "Updating repos",  # 3
    "...",  # 4
    "Updating",  # 5
    "Searching",  # 6
]


def clear():
    sys(hide[2])


class verbose:
    def all():
        hide[0] = ""
        hide[1] = ""
        hide[2] = ""

    def aur():
        hide[2] = ""
        hide[0] = ""

    def pacman():
        hide[1] = ""
        hide[2] = ""

    def quit_clear():
        hide[2] = ""


def installed():
    print(words[1])


def check(nombre_check):
    comprobator = False
    chdir(current_directoy)
    clear()
    sys("pacman -Q " + nombre_check + "> /tmp/tmp-check")
    optemp = open("/tmp/tmp-check", "r")
    readtemp = optemp.read()
    if nombre_check in readtemp:
        comprobator = True
    else:
        comprobator = False
    sys("rm /tmp/tmp-check")
    return comprobator


def install(nombre_pacman, cond_1="", cond_2=""):
    match cond_1:
        case "-v":
            print(words[0] + nombre_pacman + words[4])
            sys("sudo pacman -S " + nombre_pacman + sp + cond_2 + sp + " --noconfirm")
            print(words[1])
        case _:
            clear()
            print(words[0] + nombre_pacman + words[4])
            sys(
                "sudo pacman -S "
                + nombre_pacman
                + " --noconfirm"
                + sp
                + cond_1
                + hide[1]
            )
            clear()
            installed()


def refresh():
    clear()
    print(words[3], words[4])
    sys("sudo pacman -Syy " + hide[0])
    clear()
    print(words[2])


def remove(removes, cond_1=""):
    if check(removes) == True:
        if "v" in cond_1:
            pass
            hide[0] = ""
        if "f" in cond_1:
            sys("sudo pacman -Rdd" + sp + removes + " --noconfirm" + hide[0])
        else:
            sys("sudo pacman -R" + sp + removes + " --noconfirm" + hide[0])
    else:
        print("El o los paquetes no se encontraron en su totalidad")
    hide[0] = ">/dev/null 2>&1"


class aur:
    def install(apps_aur, cond_1=""):
        if "h" in cond_1:
            words[0, 4] = ""
        for i in apps_aur.split():
            clear()
            url = "https://aur.archlinux.org/" + i + ".git"
            chdir("/tmp")
            print("Cloning " + i + words[4])
            sys("git clone " + url + hide[0])
            clear()
            chdir(i)
            print(words[0] + i + words[4])
            sys("makepkg -si --noconfirm" + hide[0])
            clear()
            chdir(current_directoy)
            installed()

    def manager(nombre_gestor, app_gestor, cond_1="", cond_2=""):
        match cond_1:
            case "-v":
                print(words[0] + app_gestor + words[4])
                sys(
                    nombre_gestor
                    + " -S"
                    + app_gestor
                    + sp
                    + cond_2
                    + sp
                    + " --noconfirm"
                )
                print(words[1])
            case "-s":
                sys(nombre_gestor + sp + app_gestor + hide[0])
            case _:
                clear()
                print(words[0] + app_gestor + words[4])
                sys(
                    nombre_gestor
                    + " -S"
                    + app_gestor
                    + " --noconfirm"
                    + sp
                    + cond_1
                    + hide[0]
                )
                clear()
                installed()


def upgrade(condu_1="", condu_2=""):
    match condu_1:
        case "-v":
            print(words[5], words[4])
            sys("sudo pacman -Syu --noconfirm" + sp + condu_2)
        case _:
            clear()
            print(words[5], words[4])
            sys("sudo pacman -Syu --noconfirm" + sp + condu_1 + sp + hide[0])
            clear()
            print(words[2])


def get_list(list, cond1=""):
    if cond1 != "":
        options = [""]
        print(words[6], words[4])
        if "o" in cond1:
            options[0] = "Ss"
            if "e" in cond1:
                options[0] = "Si"
        else:
            if "l" in cond1:
                options[0] = "Qs"
                if "e" in cond1:
                    options[0] = "Q"
        sys("pacman -" + options[0] + sp + list)
    else:
        sys("pacman -Ss " + list)
