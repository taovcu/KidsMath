# Count to 20 by ones
import time
import sys
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.IO as io

def countObjects(m, n):
    pitem.emojiPrint(m, n)
    io.printTTS("How many {} do you see?".format(m))

    ans = io.readInt()
    if ans == n:
        io.printTTS('Correct')
    else:
        io.printTTS('Wrong')

