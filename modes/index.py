# This is the modes file. It contains all the different modes for the bot. Here is whre you will find the 
# code to process and understand user input.
#if you want to extend the functionality of the bot, this file is a good place to start

# import dependencies
from modes.baseMode import Mode
from modes.calculatorMode import Calculator
from modes.mainMode import MainMode
from typing import List
from utils import goto




#compile the modes into a list for exporting
modes: List[Mode] = [MainMode, Calculator]