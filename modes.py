
from utils import goto


class Mode:
    def __init__ (self):
        print("init mode")
        self.prompt = "main mode"
    def handleInput(self, i, modes):
        print("I don't know how to handle this")
        return goto(modes, "main")




class MainMode(Mode):
    prompt = "main mode"
    name = "main"
    def __init__(self):
        self.prompt = "main mode"
        self.name="main"
    def handleInput(self, i, modes):
        if i == "help":
            print("you need help?")
        elif i=="calc":
            return goto(modes, "calc")
        else:
            print("I didn't understand")
        return goto(modes, "main")
modes = [MainMode]