## Brightness Adjuster 
*A GTK based brightness adjuster 1.0.0*
![Icon](icons/64x64/brightness-adjuster)
## Description
-----------
Brightness Adjuster is a gtk based brightness ajuster made for linux based distros. It is a subtitute for Brightness Controller made using Qt. It features
* Red, green and blue sliders for adjusting the screen colors. 
* A notebook based UI for switching between screens. 
* A normal white brightness slider.
* Light weight
* Instant changes
* Auto screen updates (Customizable)

## Install
-------
Install using pip
```
pip install brightness-adjuster
```
Install from source
```
$ git clone https://github.com/astraldev/Brightness-Adjuster
$ cd Brightness-Adjuster
$ pip install .
```
_Coming soon to snapstore_

## Requirements
---------------
This tool requires 
- Python3 and above
`$ sudo apt install dev-python`
- PyGObect `pip3 install pygobject`
- Configparser `pip3 install configparser`
- xrandr

## Draw backs
-------------
1. This tool does not work on Wayland
2. Must not be installed globally. It must have this path format `{$HOME}/.local`
3. If not correctly installed, file links may be broken

## License
---------
This tool is shipped with the GNU Lesser public license GPL. Also see [COPYING](COPYING)

## Changelog
------------
v1.0.0
- App created
