# Utils is a file for general-purpose utility functions.
# this are base functions that aren't specific to the project

def goto(modes, name):
    return list(filter(lambda x: x.name ==name, modes))[0]