
from typing import List
from utils import goto


class Mode:
    def __init__ (self):
        print("init mode")
        self.prompt = "main mode"
    def handleInput(self, i, modes):
        print("I don't know how to handle this")
        return goto(modes, "main")
    def defaultInput(self, i, modes):
        if i == "exit" or i=="quit":
            quit(1)
        print(" I don't understand this (try doing help)")
        return goto(modes, "main")
    def init(self):
        print("changing modes...")




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
modes = [MainMode, Calculator]