# sudo python -m pip install -U pip
# sudo python -m pip install -U matplotlib
# sudo apt-get install python-tk

# Turtle graphics
import sys
import matplotlib.pyplot as plt
import numpy as np
from pictures import *
import emoji
import emojis
 
# April 16
def guessValue():
    print "Guess the value " 
    while 1:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break
    
        if not line:
            break
    
        print line
        if int(line) < a:
            print "Guessed value is too small"
            print "Guess the value again:" 
            continue
        if int(line) > a:
            print "Guessed value is too big"
            print "Guess the value again:" 
            continue
    
        print "You got it, the value is ", a 
        break
    
# print heart template
def printHeart():
    t = np.arange(0,2*np.pi, 0.1)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.plot(x,y)
    plt.show()

# April 17
def readStdin():
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        return
    while not line:
        readStdin()
    return int(line)
    
def addTest(a, b):
    print "Addition tests"
    print "%d + %d = " % (a, b)
    ans = readStdin()
    while ans != (a + b):
        print "Wrong! Please calculate the value again" 
        ans = readStdin()

    print "You got it. The correct answer is %d" %(ans)
    ballon()

def AddTestCases():    
    addTest(1, 2)
    addTest(2, 2)
    addTest(2, 7)
    addTest(2, 5)
    addTest(3, 6)
    addTest(4, 2)
    addTest(5, 7)
    addTest(6, 3)
    addTest(7, 3)
    addTest(8, 2)
    addTest(8, 7)
    addTest(9, 9)
    addTest(9, 11)

def compareItems(a, b):
    print "Count cookies"
    print emoji.emojize(':cookie: '*a), ' | ', emoji.emojize(':cookie: '*b)
    print "Do the left-side and right-side has same number of cookies? Please input y for yes, n for no"
    ans = sys.stdin.readline()[0]
    if (ans == "y" and a == b) or (ans == "n" and a != b):
        print emoji.emojize(':thumbs_up: ')*3, "You got it. Both left and right sides have %d cookies" %(a)
    else:
        print emoji.emojize(':thumbs_down: ')*3, "Wrong. Left side has %d cookies, but right side has %d cookies" %(a, b)


def main():
    print(">>>> Joy Coding Main Function")
    compareItems(4,6)


if __name__ == '__main__':
    main()
