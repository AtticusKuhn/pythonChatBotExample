# This is the main module. This file contains the most imporant code, and the code
# which will be run on program starting. You will find the main() function in this file, 
# which controls the start of the code

# import needed libraries
from typing import List
from modes import Mode, modes

# Print help text to inform the user about this project
def printHello():
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


# A class to represent the bot and its state
class Bot:
    def  __init__(self, modes: List[Mode]):
        self.modes =  modes
        self.mode = modes[0] # modes[0] is the default mode
    def ask(self):
        '''
        bot asks the user for input
        '''
        m: Mode = self.mode()
        i = input(m.prompt+ "> ") # Prompt the user for input
        newMode = m.handleInput(i, self.modes)
        if newMode.name != self.mode.name: # if the old mode is different from the new mode, we are changing modes
            n: Mode = newMode()
            n.init() # tell the user we are changing modes
        self.mode = newMode # set the new mode

# the main function is what is run when the program is started
def main():
    printHello() # print a welcome message to welcome the user
    bot = Bot(modes) # create the chat bot
    while True: 
        bot.ask() # bot asks the user for input

if __name__ == "__main__":
    main()