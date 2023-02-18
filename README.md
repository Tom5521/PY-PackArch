<img src="https://res.cloudinary.com/dqjsgmkxo/image/upload/v1676571071/Captura_de_pantalla_de_2023-02-16_15-08-13_iiarxj.png" width="1000" height="100" />


[![wakatime](https://wakatime.com/badge/github/Tom5521/PY-pacman.svg)](https://wakatime.com/badge/github/Tom5521/PY-pacman)
[![CodeFactor](https://www.codefactor.io/repository/github/tom5521/py-packarch/badge)](https://www.codefactor.io/repository/github/tom5521/py-packarch)
![GitHub repo size](https://img.shields.io/github/repo-size/Tom5521/PY-pacman)
![GitHub last commit](https://img.shields.io/github/last-commit/Tom5521/PY-pacman)


#### A Python library to be able to handle pacman package manager from Python



You can quickly add or update in to your project running this command in the folder wherever it is
```
wget https://raw.githubusercontent.com/Tom5521/PY-pacman/master/packarch.py
```
Or can install it using this command ```pip install py-packarch```

You can import it in a more comfortable way by writing ```import packarch as pacman``` at the top of the file

## Functions:

#### Check

Check if the package entered is installed

returning the True value if it is affirmative

```
check = packarch.check("spotify")
print(check)

>>>True
```
You can check several packages by separating them by spaces

#### Install

Install the packages or in the entry of the function
```
packarch.install("wine-stable neovim")
```
If you want to install more than one package you can separate through spaces
You can add more arguments after packages as I would do with Pacman
```
packarch.install("vim --needed")
```
If you want to show the exit you can put the condition ```,"-v"```
Something like that:
```
packarch.install("wine","-v")
```
If you want to add more arguments to that you will have to do something like that
```
packarch.install("wine","-v","--needed")
```


#### Refresh

It serves to update the repositories
```
packarch.refresh()
```
#### Aur.Install

It serves to install packages from the AUR
```
packarch.aur.install("visual-studio-code-bin")
```
You can put several apps to be installed for example
```
packarch.aur.install("lutris wine proton vim")
```
Las apps a instalar se tienen que separar por espacios
**possibly add the conditions in a future update**
#### Aur.Manager
This option is to install from the AUR but with a manager like Yay or Paru

Your syntax is something like that :
```
packarch.aur.manager("paru","vim base-devel","-v")
                      ^        ^             ^-Condition
                      |        |-Packages to be installed     
                      |-AUR manager 
```
- Compatible package managers:
    -yay
    -pikaur
    -paru
    -pacman(It is recommended to use ```packarch.install()```)
    -Any other that has a syntax similar to the above
Condiciones:
    "-v" It is used to see the terminal output (recommended to see errors)
    "-s" It serves to get a selector for example when you put ```yay <package>``` It is only compatible with the managers who have this function
- Upgrade

It serves to update the system and tabien can add arguments such as ```packarch.install()```

```
packarch.upgrade()
```
It also has the function to see what it does in the console adding the condition "-v", if it places the aforementioned function, if you want to add to that pacman conditions have to do it as shown forward
```
packarch.upgrade("-v","--needed --noconfirm")
```
You can also put conditions as it does in pacman

#### Remove
It serves to erase packages its syntax is following
```
packarch.remove("Package1 Package2","vf")
                   ^         ^      ^-Condition to execute 
                   |---------packages to remove
```
##### Conditions:
- "f" It serves to force the deletion of a program regardless of what apps depend on it
- "v" It serves to see pacman exit
Conditions can be combined regardless of order
#### Verbose
What it does is that the exit of the console is seen to the functions of the library
##### Functions:
- ```verbose.all()``` makes all installation operations show their output on console
- ```verbose.aur()``` makes all operations regarding the AURs show their exit in console
- ```verbose.pacman()``` makes all installation operations of ```packarch.install``` are shown in the console
- ```verbose.quit_clear``` Remove the terminal cleaning
#### An example of syntax
```
packarch.aur.install("wine") #Does not show output on the console

packarch.verbose.aur()
packarch.aur.install("grapejuice") #This you see if it shows the exit on the console
#It is used in the same way with its other functions previously explained
```

#### Get List

An example of its syntax
```
packarch.get_list("package names","condition")
```
##### Conditions
- ```o``` search in repositories
- ```l``` search locally
- Above conditions + ```e``` :Take out a description of the package depending on the first condition 
### Adding some extra data:
This project was created as a dipurcation of my other project named [**Arch-App-Installer**](https://github.com/Tom5521/Arch-App-Installer)
And this project will apparently take its own path since the packarch.py of the project mentioned above will stay in version 1.0.0 for syntax issues
or maybe take your own course adapting to that project
For now that's all

#### PD:
### I still without ideas 

<img src="https://miro.medium.com/v2/resize:fit:400/0*BZKe97Qy_Z_jCqwu.gif">
