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

