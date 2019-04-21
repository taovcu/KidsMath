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

def addTest(a, b):
    print "%d + %d = " % (a, b)
    ans = io.readStdin()
    while ans != (a + b):
        print "Wrong! Please calculate the value again"
        ans = io.readStdin()

    print "You got it. The correct answer is %d" %(ans)

def subtractTest(a, b):
    ans = io.readStdin()
    while ans != (a - b):
        print emoji.emojize(':thumbs_down: :thumbs_down: :thumbs_down: '), "Wrong! Please calculate the value again"
        ans = io.readStdin()

    print emoji.emojize(':thumbs_up: :thumbs_up: :thumbs_up: '), "You got it. The correct answer is %d" %(ans)

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
