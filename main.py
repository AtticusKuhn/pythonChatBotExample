from typing import List
from modes import Mode, modes


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



class Bot:
    def  __init__(self, modes: List[Mode]):
        self.modes =  modes
        self.mode = modes[0]
    def ask(self):
        m: Mode = self.mode()
        i = input(m.prompt+ "> ")
        newMode = m.handleInput(i, self.modes)
        if newMode.name != self.mode.name:
            n = newMode()
            n.init()
        self.mode = newMode
def main():
    printHello()
    bot = Bot(modes)
    for i in range(10):
        bot.ask()

if __name__ == "__main__":
    main()