# Creado por Tom5521 o Angel pa'los cuates
# Bajo la licencia GPL 3.0

# PY-pacman https://github.com/Tom5521/PY-pacman

# V1.4.0

from os import getcwd, chdir
from os import system as sys
from time import sleep as sl

current_directoy = getcwd()

hide = [">/dev/null 2>&1"]
sinc = " -S "
sp = " "


def clear():
    sys("clear")


def installed():
    print("Instalado")
    sl(1)


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
            print("Instalando " + nombre_pacman + "...")
            sys("sudo pacman -S " + nombre_pacman + sp + cond_2 + sp + " --noconfirm")
            print("Instalado")
        case _:
            clear()
            print("Instalando " + nombre_pacman + "...")
            sys(
                "sudo pacman -S "
                + nombre_pacman
                + " --noconfirm"
                + sp
                + cond_1
                + "|ls > .out && rm -rf .out"
            )
            clear()
            installed()


def refresh():
    clear()
    print("Actualizando repos...")
    sys("sudo pacman -Syy " + hide[0])
    clear()
    print("Repos Actualizados")


def remove(removes, cond_1=""):
    match cond_1:
        case "-v":
            sys("sudo pacman -R" + sp + removes + " --noconfirm")
        case "-f":
            sys("sudo pacman -Rdd" + sp + removes + " --noconfirm" + hide[0])
        case _:
            sys("sudo pacman -R" + sp + removes + " --noconfirm" + hide[0])


class aur:
    def install(apps_aur):
        for i in apps_aur.split():
            clear()
            url = "https://aur.archlinux.org/" + i + ".git"
            chdir("/tmp")
            print("Clonando " + i + "...")
            sys("git clone " + url + hide[0])
            clear()
            chdir(i)
            print("Instalando " + i + "...")
            sys("makepkg -si --noconfirm" + hide[0])
            clear()
            chdir(current_directoy)
            installed()

    def manager(nombre_gestor, app_gestor, cond_1="", cond_2=""):
        match cond_1:
            case "-v":
                print("Instalando " + app_gestor + "...")
                sys(
                    nombre_gestor
                    + sinc
                    + app_gestor
                    + sp
                    + cond_2
                    + sp
                    + " --noconfirm"
                )
                print("Instalado")
            case "-s":
                sys(nombre_gestor + sp + app_gestor + hide[0])
            case _:
                clear()
                print("Instalando " + app_gestor + "...")
                sys(
                    nombre_gestor
                    + sinc
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
            print("Actualizando...")
            sys("sudo pacman -Syu --noconfirm" + sp + condu_2)
        case _:
            clear()
            print("Actualizando...")
            sys("sudo pacman -Syu --noconfirm" + sp + condu_1 + sp + hide[0])
            clear()
            print("Actualizacion Completada")
