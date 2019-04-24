import sys
sys.path.append('../../')

import time
import emoji
import Helpers.IO as io

def countNumfromX(x, y):
    io.printTTS("Count from {} to {}, leave a blank between numbers".format(x, y))
    ans = sys.stdin.readline()
    ans = ans.split()
    ans = map(int, ans)
    if ans == range(x, y+1):
        io.printTTS(emoji.emojize(':thumbs_up: ')*3, "You got it.")
    else:
        io.printTTS(emoji.emojize(':thumbs_down: ')*3, "The correct sequence is ", [i for i in range(x, y+1)])

