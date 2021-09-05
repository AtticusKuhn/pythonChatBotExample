# This is the main module. This file contains the most imporant code, and the code
# which will be run on program starting. You will find the main() function in this file, 
# which controls the start of the code

# import needed libraries
from bot import Bot # the bot class
from typing import List # a list type
from modes.baseMode import Mode # a mode
from modes.index import modes # the list of modes

def main():# the main function is what is run when the program is started
    bot = Bot(modes) # create the chat bot
    bot.printHello()  # print a welcome message to welcome the user
    while True:  # make the bot run forever
        bot.ask() # bot asks the user for input

if __name__ == "__main__": # run the program if this is the main file
    main()