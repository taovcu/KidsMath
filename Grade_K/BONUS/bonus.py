import sys
sys.path.append('../../')

import time
import matplotlib.pyplot as plt
import numpy as np
import emoji

import Helpers.IO as io

# Designed on April 16, 2019
def guessValue(a):
    while 1:
        try:
            line = io.readInt()
        except KeyboardInterrupt:
            break
    
        if not line:
            break
    
        if line < a:
            print("Guessed value is too small")
            print("Guess the value again:")
            continue
        if line > a:
            print("Guessed value is too big")
            print("Guess the value again:")
            continue
    
        print("You got it, the value is ", a)
        break

def addTest(a, b):
    print("{} + {} = ".format(a, b))
    ans = io.readInt()
    while ans != (a + b):
        print("Wrong! Please calculate the value again")
        ans = io.readInt()

    print("You got it. The correct answer is {}".format(ans))

def subtractTest(a, b):
    ans = io.readInt()
    while ans != (a - b):
        print(emoji.emojize(':thumbs_down: :thumbs_down: :thumbs_down: '), "Wrong! Please calculate the value again")
        ans = io.readInt()

    print(emoji.emojize(':thumbs_up: :thumbs_up: :thumbs_up: '), "You got it. The correct answer is %d" %(ans))

def compareItems(a, b, item):
    print("Count ", item)
    print(emoji.emojize((':'+item+': ') *a), ' | ', emoji.emojize((':'+item+': ') *b))
    print('Do the left-side and right-side has same number of {}? Please input y for yes, n for no'.format(item))
    ans = sys.stdin.readline()[0]
    while ans not in ['n', 'N', 'y', 'Y']:
        print("You can only input 'n' or 'y'")
        ans = sys.stdin.readline()[0]
    if (ans in ['y', 'Y'] and a == b):
        print(emoji.emojize(':thumbs_up: ')*3, "You got it. Both left and right sides have {} {}".format(a,item))
    elif (ans in ['n', 'N'] and a != b):
        print(emoji.emojize(':thumbs_up: ')*3, "You got it. Left side has {} {}, but right side has {} {}".format(a,item, b,item))
    else:
        print(emoji.emojize(':thumbs_down: ')*3, "Wrong. Left side has %d %s, but right side has {} {}" %(a,item, b,item))

    input("Press Enter to continue...")
