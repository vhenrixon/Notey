#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import sys
from pyfiglet import Figlet


"""
Author: Vhenrixon 
What is this: A simple a CLI for a generating a template note file
"""
BOLD = '\033[1m'

def generate_file(dispatch, flags):
    # Command to create a file with a template for notes in Markdown 
    if flags is not None:
        flag = _flag_dict(flags)
        if "-n" or "-name" in flag:
            name = flag["-n"] or flag["-name"]
            with open(name+".md", "w") as f:
                f.write(f"# {name} \n --- ")
            return f"Created {name} file!"
    else:
        return "The Generate command needs flags"


def generate_help(dispatch):
    # generates a help menu from the info inside of the dispatch
    f = Figlet(font='slant')
    print(f.renderText('Notes-CLI'))
    help_text = f"\n{BOLD}Help"
    for commands in dispatch:
        help_text += f"\n { commands } \n\t Discription: {dispatch[commands]['discription']} \n\t Flags: { dispatch[commands]['flags']}"
    return help_text


dispatch = {
    # The dispatch dictionary holds the command has the value and then attributes of the command has values 
    """
    EXAMPLE:
    COMMAND : {
        "keys": [array of the alternative keys that the command can use],
        "flags": [array of the flags that a command can have],
        "function": points to the function that should fire because the command was run,
        "discription": A discription of the command that will be used inside of the help menu
    }
    """

    "generate": {
        "keys": ["g", "gen"],
        "flags": ['-n', '-name', ],
        "function": generate_file,
        "discription": "Generates the mark down for note taking",
    },
    "--help": {
        "keys": ["h"],
        "flags": [],
        "function": generate_help,
        "discription": "Generates the help menu",
    },
}


def _flag_dict(flag_arr):
    # Converts a array of flag and value pairs into a dictionary
    flag_dict = {}
    i = 0
    while i < len(flag_arr):
        flag_dict[flag_arr[i]] = flag_arr[i+1]
        i += 2
    return flag_dict


def _isAltKey(arg):
    # Checks to see if an the arg is a commands alternative key 
    for commands in dispatch:
        if arg in dispatch[commands]["keys"]:
            return commands
    return None

def _has_flags(command):
    # Checks to see if the command in question has flags
    if(len(dispatch[command]["flags"]) > 0):
        return True
    else:
        return False


def main():
    for i, arg in enumerate(sys.argv):
        altKey = _isAltKey(arg)
        if arg in dispatch:  # Is the base command
            if _has_flags(arg):
                print(dispatch[arg]['function'](
                    dispatch, [flags for flags in sys.argv[i+1: len(sys.argv)]]))
            else:
                print(dispatch[arg]['function'](dispatch))
        elif altKey is not None:  # Is a Alt key of the base commands
            if _has_flags(altKey):
                print(dispatch[altKey]['function'](
                    dispatch, [flags for flags in sys.argv[i+1: len(sys.argv)]]))
            else:
                print(dispatch[altKey]['function'](dispatch))


if __name__ == "__main__":
    main()
