# This is the modes file. It contains all the different modes for the bot. Here is whre you will find the 
# code to process and understand user input.
#if you want to extend the functionality of the bot, this file is a good place to start

# import dependencies
from typing import List
from utils import goto

# the base mode class 
class Mode:
    def __init__ (self):
        print("init mode")
        self.prompt = "main mode"
    def handleInput(self, i, modes):
        '''
        Handle input from the user once it has been recieved
        '''
        print("I don't know how to handle this")
        return goto(modes, "main")
    def defaultInput(self, i, modes):
        '''
        The default handler for user input if no other handler has been specified
        '''
        if i == "exit" or i=="quit":
            quit(1)
        print(" I don't understand this (try doing help)")
        return goto(modes, "main")
    def init(self):
        '''
        Inform the user when the bot is changing modes
        '''
        print("changing modes...")



# the main mode, the mode the user is put into on startup
class MainMode(Mode):
    prompt = "main mode"
    name = "main"
    def __init__(self):
        self.prompt = "main mode"
        self.name="main"
    def handleInput(self, i, modes):
        if i == "help":
            print('''hello my name is PHP (python helper person), and I can help you. I have several modes 
     and I am designed to be the ideal chatbot and personal assistant. To see what I can do,
     type "help", and to find some calculations, type "calc".''')
            return MainMode
        elif i=="calc":
            return goto(modes, "calc")
        else:
            return self.defaultInput(i, modes)
    def init(self):
        print("the main mode handes all primary functionality")

#a calculator app
class Calculator(Mode):
    prompt = "calc mode"
    name = "calc"
    def __init__(self):
        self.prompt = "calc mode"
        self.name="calc"
    def handleInput(self, i, modes):
        if i == "1+1":
            print("2")
            return Calculator
        else:
            return self.defaultInput(i, modes)
    def init(self):
        print("the calculator is good for simple calculations")
#compile the modes into a list for exporting
modes = [MainMode, Calculator]