# ScummVM - GDB
Pretty printers for ScummVM's 'Common' types

## Requirements
* Python 3
* Recent GDB

## Usage
1. Create a .gdbinit file in the directory where the ScummVM-ish executable you want to debug is located to instruct GDB to load the pretty printer script:

    source /path/to/scummvm-gdb/gdb-pretty-printers.py

2. Instruct GDB to trust the .gdbinit file you just created by adding its path to the whitelist in the .gdbinit file in your home directory:

    add-auto-load-safe-path /path/to/scummvm/.gdbinit
