import sys
sys.path.append('../../')

import Helpers.IO as io
import time
import random
import string
import emoji


def countNumby10s(m, t):
    io.printTTS("Count from 10 up to {} by 10 s".format(m))
    
    # if t == 1, randomly skip a number 
    if t:
        t = (int)(random.SystemRandom().choice(string.digits)) * 10
        
    for i in range(10, m+1, 10):
        if i == t:
            continue
        io.printTTS(str(i))
        # wait for 1 second
        time.sleep(1)

    io.printTTS('Is there any number missing in this sequence? Say yes or no')
    ans = io.readLine()
    if ans not in ['yes', 'no']:
        io.printTTS('Is there any number missing in this sequence? Please input from keyboard: y for yes, n for no')
        ans = io.readChar()
   
    while ans not in ['yes', 'no', 'y', 'n']:
        io.printTTS('Please input from keyboard: y for yes, n for no')
        ans = io.readChar()

    if (ans in ['yes', 'y'] and t):
        io.printTTS(emoji.emojize(':thumbs_up: ')*3 + "You got it. {} is missing".format(t))
    elif (ans in ['no', 'n'] and not t):
        io.printTTS(emoji.emojize(':thumbs_up: ')*3 + "You got it. All numbers are there")
    else:
        if ans in ['yes', 'y']: 
            io.printTTS(emoji.emojize(':thumbs_down: ')*3 + "Wrong. You say there is some number missing, but actually all numbers are in the sequence")
        if ans in ['no', 'n']: 
            io.printTTS(emoji.emojize(':thumbs_down: ')*3 + "Wrong. You say there is no number missing, but actually {} is NOT in the sequence".format(t))
