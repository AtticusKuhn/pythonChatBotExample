# Utils is a file for general-purpose utility functions.
# this are base functions that aren't specific to the project

#Import Dependencies
from typing import List
from modes import Mode

# given modes and a mode name, goto that mode with the name
def goto(modes: List[Mode], name: str) -> Mode:
    return list(filter(lambda x: x.name ==name, modes))[0]