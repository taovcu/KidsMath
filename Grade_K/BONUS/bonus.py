import sys
sys.path.append('../../')

import time
import matplotlib.pyplot as plt
import numpy as np
import emoji

import Helpers.IO as io

# Designed on April 16, 2019
def guessValue(a):
    io.printTTS("Guess value in range 100")

    while 1:
        try:
            line = io.readInt()
        except KeyboardInterrupt:
            break
    
        if not line:
            break
    
        if line < a:
            io.printTTS("Guessed value is too small")
            io.printTTS("Guess the value again:")
            continue
        if line > a:
            io.printTTS("Guessed value is too big")
            io.printTTS("Guess the value again:")
            continue
    
        io.printTTS("You got it, the value is {}".format(a))
        break

def addTest(a, b):
    io.printTTS("Calculate a + b")
    io.printTTS("{} + {} = ".format(a, b))
    ans = io.readInt()
    while ans != (a + b):
        io.printTTS("Wrong! Please calculate the value again")
        ans = io.readInt()

    io.printTTS("You got it. The correct answer is {}".format(ans))

def subtractTest(a, b):
    io.printTTS("Calculate a - b")
    io.printTTS("{} - {} = ".format(a, b))
    ans = io.readInt()
    while ans != (a - b):
        io.printTTS(emoji.emojize(':thumbs_down: :thumbs_down: :thumbs_down: '), "Wrong! Please calculate the value again")
        ans = io.readInt()

    io.printTTS(emoji.emojize(':thumbs_up: :thumbs_up: :thumbs_up: ') + "You got it. The correct answer is {}".format(ans))

def compareItems(a, b, item):
    io.printTTS("Count {}".format(item))
    print(emoji.emojize((':'+item+': ') *a), ' | ', emoji.emojize((':'+item+': ') *b))
    io.printTTS('Do the left-side and right-side has same number of {}? Please input y for yes, n for no'.format(item))
    ans = io.readChar()
    while ans not in ['n', 'N', 'y', 'Y']:
        print("You can only input 'n' or 'y'")
        ans = io.readChar()
    if (ans in ['y', 'Y'] and a == b):
        print(emoji.emojize(':thumbs_up: ')*3, "You got it. Both left and right sides have {} {}".format(a,item))
    elif (ans in ['n', 'N'] and a != b):
        print(emoji.emojize(':thumbs_up: ')*3, "You got it. Left side has {} {}, but right side has {} {}".format(a,item, b,item))
    else:
        print(emoji.emojize(':thumbs_down: ')*3, "Wrong. Left side has %d %s, but right side has {} {}" %(a,item, b,item))
