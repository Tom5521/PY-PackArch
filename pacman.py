
from os import getcwd,chdir
from os import system as sys
from time import sleep as sl
current_directoy = (getcwd())

def clear(): sys("clear")

def installed():
    print("Instalado")
    sl(1)


def check(nombre_check):
    comprobator = False
    chdir(current_directoy)
    clear()
    sys("pacman -Q "+ nombre_check + "> src/temp")
    optemp = open("src/temp","r")
    readtemp = optemp.read()
    if nombre_check in readtemp: comprobator = True
    else: comprobator = False
    sys("rm src/temp")
    return comprobator

def install(nombre_pacman):
    clear()
    print("Instalando " + nombre_pacman + "...")
    sys("sudo pacman -S " + nombre_pacman + " --noconfirm|ls > .out && rm -rf .out")
    clear()
    installed()

def refresh():
    clear()
    print("Actualizando repos...")
    sys("sudo pacman -Syy >/dev/null 2>&1")
    clear()
    print("Repos Actualizados")

def aur(nombre_aur):
    clear()
    url = "https://aur.archlinux.org/" + nombre_aur + ".git"
    chdir("/tmp")
    print("Clonando " + nombre_aur + "...")
    sys("git clone "+ url + ">/dev/null 2>&1")
    clear()
    chdir(nombre_aur)
    print("Instalando " + nombre_aur + "...")
    sys("makepkg -si --noconfirm >/dev/null 2>&1")
    clear()
    chdir(current_directoy)
    installed()

def upgrade():
    clear()
    print("Actualizando...")
    sys("sudo pacman -Syu --noconfirm >/dev/null 2>&1")
    clear()
    print("Actualizacion Completada")