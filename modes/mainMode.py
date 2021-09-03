from typing import List
from modes.baseMode import Mode
from utils import goto
# the main mode, the mode the user is put into on startup
class MainMode(Mode):
    prompt = "main mode"
    name = "main"
    def __init__(self):
        self.prompt = "main mode"
        self.name="main"
    def handleInput(self, i, modes: List[Mode]) -> Mode:
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
