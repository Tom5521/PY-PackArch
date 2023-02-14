<img src="https://github.com/Tom5521/PY-pacman/blob/82a8b8ea22d748ab728b7acbf174562c9adf2f72/PY-pacman.png" width="1000" height="100" />

#### Una libreria de python para poder manejar el gestor de paquetes pacman desde python

## Funciones:

#### Check

Comprueba si el o los paquetes estan instalados

devolviendo el valor True si es Afirmativo

```
check = pacman.check("spotify")
print(check)

>>>True
```
Puedes comprobar varios paquetes separandolos por espacios

#### Install

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


#### Refresh

Sirve para Actualizar los repositorios
```
pacman.refresh()
```
- AUR.INSTALL

Sirve para instalar paquetes desde los AUR
```
pacman.aur.install("visual-studio-code-bin")
```
se pueden poner varias apps a instalar por ejemplo
```
pacman.aur.install("lutris wine proton vim")
```
Las apps a instalar se tienen que separar por espacios
**posiblemente añada las condiciones en una futura actualizacion**
#### AUR.MANAGER
Esta opcion es para instalar desde los aur pero con un gestor como yay o paru

Su sintaxis es mas o menos asi
```
pacman.aur.manager("paru","vim base-devel","-v")
                      ^        ^             ^- Condicion
                      |        |- Paquetes a instalar     
                      |- Gestor de paquetes a usar 
```
- Gestores de paquetes compatibles:
    -yay
    -pikaur
    -paru
    -pacman(se recomienda usar ```pacman.install()```)
    -cualquier otro que tenga una sintaxis similar a las anteriores
Condiciones:
    "-v" se usa para ver la salida del terminal(recomendado para ver errores)
    "-s" sirve para sacar un selector por ejemplo cuando pones ```yay <paquete>``` solo es compatible con los gestores que tienen esta funcion
- Upgrade

Sirve para actualizar el sistema y tabien puede añadir argumentos como a ```pacman.install()```

```
pacman.upgrade()
```
Tambien tiene la funcion para ver lo que hace en la consola añadiendo la condicion "-v",si coloca la funcion anteriormente mencionada,si quiere sumarle a eso condiciones de pacman tiene que hacerlo como se muestra adelante
```
pacman.upgrade("-v","--needed --noconfirm")
```
Tambien puede poner condiciones como lo hace en pacman

#### Remove
Sirve para borrar paquetes su sintaxis es la siguiente
```
pacman.remove("paquete2 paquete2","-f")
                   ^         ^      ^-Conficion a Ejecutar 
                   |---------Nombres de paquetes a borrar
```
##### Condiciones:
- "-f " sirve para forzar el borrado de un programa sin importar que apps dependan de ella
- "-v " sirve para ver la salida de pacman

#### Verbose
Lo que hace es que se vea la salida de la consola a funciones de la libreria
##### Funciones
- ```verbose.all()``` hace que todas las operaciones de instalacion muestren su salida en consola
- ```verbose.aur()``` hace que todas las operaciones con respecto a los aur muestren su salida en consola
- ```verbose.pacman()``` hace que todas las operaciones de instalacion de ```pacman.install``` se muestren en la consola
#### Un ejemplo de la sintaxis
```
pacman.aur.install("wine") #no muestra salida en la consola

pacman.verbose.aur()
pacman.aur.install("grapejuice") #Esta ves si muestra la salida en la consola
#Se usa de la misma manera con sus otras funciones anteriormente explicadas
```
### Añadiendo un poco de data extra:
Este proyecto fue creado como una difurcacion de mi otro proyecto osea **Arch-Instalator**
Y este proyecto al parecer tomara su propio camino ya que el pacman.py del proyecto mencionado anteriormente se quedara en la version 1.0.0 por temas de sintaxis
o tal vez tome su propio rumbo adaptandose a ese proyecto
por ahora eso es todo

#### PD:
### Sigo sin ideas 