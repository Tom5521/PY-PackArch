<img src="https://github.com/Tom5521/PY-pacman/blob/82a8b8ea22d748ab728b7acbf174562c9adf2f72/PY-pacman.png" width="1000" height="100" />

#### Una libreria de python para poder manejar el gestor de paquetes pacman desde python

Funciones:

- Check

Comprueba si el o los paquetes estan instalados

devolviendo el valor True si es Afirmativo

```
check = pacman.check("spotify")
print(check)

>>>True
```
Puedes comprobar varios paquetes separandolos por espacios

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
si quiere mostrar la salida puede poner de condicion ```,"-v"```
Algo asi:
```
pacman.install("wine","-v")
```
si quiere añadir mas argumentos a eso tendra que hacer algo asi
```
pacman.install("wine","-v","--needed")
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
se pueden poner varias cosas a instalar por ejemplo
```
pacman.aur("lutris","wine","spotify")
```
Solo se pueden poner hasta tres cosas a la vez
lamentablemente no acepta condiciones
**posiblemente añada las condiciones en una futura actualizacion**
- Upgrade

Sirve para actualizar el sistema y tabien puede añadir argumentos como a ```pacman.install()```

```
pacman.upgrade()
```
Al igual que con ```pacman.aur()``` no acepta condiciones y repito **posiblemente añada las condiciones en una futura actualizacion**
