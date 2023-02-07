# PY-pacman

Una libreria de python para poder manejar el gestor de paquetes pacman desde python

Funciones:

- Check

Comprueba si el o los paquetes estan instalados

```
pacman.check("paquete")
```

- Install

Instala el o los paquetes puestos en la entrada de la funcion
```
pacman.install("wine-stable neovim")
```
si quiere instalar mas de un paquete puede separarlo por espacios
Puede añadir mas argumentos despues de los paquetes como lo haria con pacman
```
pacman.install("vim --needed")
```
- Refresh

Sirve para Actualizar los repositorios
```
pacman.refresh()
```
- AUR

Sirve para instalar paquetes desde los AUR
```
pacman.aur("visual-studio-code-bin")
```
lamentablemente solo se pueden instalar uno ala vez y no acepta condiciones
**posiblemente añada las condiciones en una futura actualizacion**
- Upgrade

Sirve para actualizar el sistema y tabien puede añadir argumentos como a ```pacman.install()```

```
pacman.upgrade()
```
Al igual que con ```pacman.aur()``` no acepta condiciones y repito **posiblemente añada las condiciones en una futura actualizacion**
