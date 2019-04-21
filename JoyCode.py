# sudo python -m pip install -U pip
# sudo python -m pip install -U matplotlib
# sudo apt-get install python-tk

# Turtle graphics
import sys
import time
sys.path.append('.')

import matplotlib.pyplot as plt
import numpy as np
from pictures import *
import emoji

import Grade_K.KCC1_3._00_NumberNames as KCC0
import Grade_K.KCC1_3._01_CountTo100By10s as KCC1
import Grade_K.KCC1_3._02_CountfromX as KCC2
import Grade_K.KCC1_3._03_CountTo20 as KCC3

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

def donutprint():
    # create data
    size_of_groups=[1]

    # Create a pieplot
    plt.pie(size_of_groups, colors = ['orange'])
    #plt.show()
    
    # add a circle at the center
    my_circle=plt.Circle( (0,0), 0.4, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    
    plt.show()
 
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

def subtractTest(a, b):
    print "Subtraction tests"
    print "%d - %d = " % (a, b)
    ans = readStdin()
    while ans != (a - b):
        print emoji.emojize(':thumbs_down: :thumbs_down: :thumbs_down: '), "Wrong! Please calculate the value again"
        ans = readStdin()

    print emoji.emojize(':thumbs_up: :thumbs_up: :thumbs_up: '), "You got it. The correct answer is %d" %(ans)

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

def subtractTestCases():
    subtractTest(2, 2)
    subtractTest(7, 2)
    subtractTest(5, 2)
    subtractTest(6, 3)
    subtractTest(4, 2)
    subtractTest(7, 5)
    subtractTest(6, 3)
    subtractTest(7, 3)
    subtractTest(8, 2)
    subtractTest(8, 7)
    subtractTest(9, 9)
    subtractTest(15, 11)
    subtractTest(19, 3)
    ballon()

def compareTestCases():
    compareItems(4,6,'cookie')
    compareItems(7,8,'princess')
    compareItems(9,7,'baby')
    compareItems(10,10,'turtle')
    compareItems(13,12,'crocodile')
    
def compareItems(a, b, item):
    print "Count ", item
    print emoji.emojize((':'+item+': ') *a), ' | ', emoji.emojize((':'+item+': ') *b)
    print 'Do the left-side and right-side has same number of %s? Please input y for yes, n for no' %(item)
    ans = sys.stdin.readline()[0]
    while ans not in ['n', 'N', 'y', 'Y']:
        print "You can only input 'n' or 'y'" 
        ans = sys.stdin.readline()[0]
    if (ans in ['y', 'Y'] and a == b):
        print emoji.emojize(':thumbs_up: ')*3, "You got it. Both left and right sides have %d %s" %(a,item)
    elif (ans in ['n', 'N'] and a != b):
        print emoji.emojize(':thumbs_up: ')*3, "You got it. Left side has %d %s, but right side has %d %s" %(a,item, b,item)
    else:
        print emoji.emojize(':thumbs_down: ')*3, "Wrong. Left side has %d %s, but right side has %d %s" %(a,item, b,item)

    raw_input("Press Enter to continue...")


def main():
    print(">>>> Joy Coding Main Function")
    KCC0.Number2Name(3)
    KCC1.countNumby10s(40, 1)
    KCC2.countNumfromX(3, 5)
    KCC3.countNum(6)

if __name__ == '__main__':
    main()
