# This file contains the bot class, which is a class representing the bot
# it contains the state and methods related to interacting with the bot.


# import needed libraries
from typing import List
from modes.baseMode import Mode
from modes.index import modes

class Bot:# A class to represent the bot and its state
    name = "php"
    def  __init__(self, modes: List[Mode]):
        self.modes =  modes
        self.mode = modes[0] # modes[0] is the default mode
    # Print help text to inform the user about this project
    def printHello(self):
        '''
        Print help text to inform the user about this project
        '''
        print(
''' ________  ___  ___  ________   
|\   __  \|\  \|\  \|\   __  \  
\ \  \|\  \ \  \\\  \ \  \|\  \ 
\ \   ____\ \   __  \ \   ____\\
\ \  \___|\ \  \ \  \ \  \___|
\ \__\    \ \__\ \__\ \__\   
\|__|     \|__|\|__|\|__|  
hello my name is PHP (python helper person), and I can help you. I have several modes 
and I am designed to be the ideal chatbot and personal assistant. To see what I can do,
    type "help", and to find some calculations, type "calc".''')
    def ask(self):
        '''
        bot asks the user for input
        '''
        m: Mode = self.mode()
        i = input(f'{self.name}: {m.prompt}>') # Prompt the user for input
        newMode = m.handleInput(i, self.modes)
        if newMode.name != self.mode.name: # if the old mode is different from the new mode, we are changing modes
            n: Mode = newMode()
            n.init() # tell the user we are changing modes
        self.mode = newMode # set the new mode

