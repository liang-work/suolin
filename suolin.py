## coding: utf-8
## suolin.py

## Import standard modules
import os
import sys
import time

## Import necessary modules
try:
    import rich
    from rich import console
except ImportError:
    print("[ERROR]: Some important modules are missing. Please run 'pip install -r requirements.txt' to install them.")

## Initialize the console
console = console.Console()

## Import internal modules
try:
    import readFile
    import langToLocal
except ImportError:
    console.print("[bold red][ERROR][/bold red]: some internal modules are missing. Please try fix this or reinstall the application.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pass
