<img src="https://github.com/Tom5521/PY-pacman/blob/82a8b8ea22d748ab728b7acbf174562c9adf2f72/PY-pacman.png" width="1000" height="100" />


#### A Python library to be able to handle pacman package manager from Python


[![wakatime](https://wakatime.com/badge/github/Tom5521/PY-pacman.svg)](https://wakatime.com/badge/github/Tom5521/PY-pacman)
[![CodeFactor](https://www.codefactor.io/repository/github/tom5521/py-pacman/badge)](https://www.codefactor.io/repository/github/tom5521/py-pacman)
![GitHub repo size](https://img.shields.io/github/repo-size/Tom5521/PY-pacman)
![GitHub last commit](https://img.shields.io/github/last-commit/Tom5521/PY-pacman)





You can quickly add it to your project by running this command in the folder wherever it is
```
wget https://raw.githubusercontent.com/Tom5521/PY-pacman/master/pacman.py
```

## Functions:

#### Check

Check if the package entered is installed

returning the True value if it is affirmative

```
check = pacman.check("spotify")
print(check)

>>>True
```
You can check several packages by separating them by spaces

#### Install

Install the packages or in the entry of the function
```
pacman.install("wine-stable neovim")
```
If you want to install more than one package you can separate through spaces
You can add more arguments after packages as I would do with Pacman
```
pacman.install("vim --needed")
```
If you want to show the exit you can put the condition ```,"-v"```
Something like that:
```
pacman.install("wine","-v")
```
If you want to add more arguments to that you will have to do something like that
```
pacman.install("wine","-v","--needed")
```


#### Refresh

It serves to update the repositories
```
pacman.refresh()
```
#### Aur.Install

It serves to install packages from the AUR
```
pacman.aur.install("visual-studio-code-bin")
```
You can put several apps to be installed for example
```
pacman.aur.install("lutris wine proton vim")
```
Las apps a instalar se tienen que separar por espacios
**possibly add the conditions in a future update**
#### Aur.Manager
This option is to install from the AUR but with a manager like Yay or Paru

Its syntax is more or less like that
```
pacman.aur.manager("paru","vim base-devel","-v")
                      ^        ^             ^-Condition
                      |        |-Packages to be installed     
                      |-AUR manager 
```
- Compatible package managers:
    -yay
    -pikaur
    -paru
    -pacman(It is recommended to use ```pacman.install()```)
    -Any other that has a syntax similar to the above
Condiciones:
    "-v" It is used to see the terminal output (recommended to see errors)
    "-s" It serves to get a selector for example when you put ```yay <package>``` It is only compatible with the managers who have this function
- Upgrade

It serves to update the system and tabien can add arguments such as ```pacman.install()```

```
pacman.upgrade()
```
It also has the function to see what it does in the console adding the condition "-v", if it places the aforementioned function, if you want to add to that pacman conditions have to do it as shown forward
```
pacman.upgrade("-v","--needed --noconfirm")
```
You can also put conditions as it does in pacman

#### Remove
It serves to erase packages its syntax is following
```
pacman.remove("Package1 Package2","-f")
                   ^         ^      ^-Condition to execute 
                   |---------packages to remove
```
##### Conditions:
- "-f " It serves to force the deletion of a program regardless of what apps depend on it
- "-v " It serves to see pacman exit

#### Verbose
What it does is that the exit of the console is seen to the functions of the library
##### Functions:
- ```verbose.all()``` makes all installation operations show their output on console
- ```verbose.aur()``` makes all operations regarding the AURs show their exit in console
- ```verbose.pacman()``` makes all installation operations of ```pacman.install``` are shown in the console
#### An example of syntax
```
pacman.aur.install("wine") #Does not show output on the console

pacman.verbose.aur()
pacman.aur.install("grapejuice") #This you see if it shows the exit on the console
#It is used in the same way with its other functions previously explained
```
### Añadiendo un poco de data extra:
This project was created as a dipurcation of my other project named **Arch-Instalator**
And this project will apparently take its own path since the pacman.py of the project mentioned above will stay in version 1.0.0 for syntax issues
or maybe take your own course adapting to that project
For now that's all

#### PD:
### I still without ideas 
