# Utils is a file for general-purpose utility functions.
# this are base functions that aren't specific to the project

#Import Dependencies
from typing import List

# given modes and a mode name, goto that mode with the name
def goto(modes, name: str):
    return list(filter(lambda x: x.name ==name, modes))[0]