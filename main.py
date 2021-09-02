from modes import modes


def printHello():
    print("hello my name is PHP (python helper person), and I can help you")



class Bot:
    def  __init__(self, modes):
        self.modes =  modes
        self.mode = modes[0]
    def ask(self):
        m = self.mode()
        i = input(m.prompt)
        self.mode = m.handleInput(i, self.modes)
def main():
    printHello()
    bot = Bot(modes)
    for i in range(10):
        bot.ask()

if __name__ == "__main__":
    main()