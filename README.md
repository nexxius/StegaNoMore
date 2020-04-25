# StegaNoMore

StegaNoMore is a simple command line tool to automatically solve steganography puzzles and uncover hidden information. It was designed to quickly run several tests on a specified file to find hidden information. It is particularly useful for capture the flag (CTF) challenges.

## Dependencies
StegaNoMore only supports Linux. So far it has only been tested on a default Kali Linux installation. 
The following packages must be installed:
* python3
* strings
* steghide
* fcrackzip
* imagemagick
* [stegcracker](https://github.com/Paradoxis/StegCracker)

The wordlist `rockyou.txt` must also be located in `/usr/share/wordlists`.

## Installation
You can download StegaNoMore with:
```
git clone https://github.com/nexxius/StegaNoMore.git
```

## Useage
StegaNoMore can be used with the following command:
```
python3 steganomore.py [/path/to/targetfile.extension]
```

## License
Copyright 2020 - Nick Delcore (Nexxius)

StegaNoMore is licensed under the [GNU General Public License Version 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) or any later version as published by the Free Software Foundation.
