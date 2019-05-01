# Count to 20 by ones
import time
import sys
sys.path.append('../../')

import inflect
import Helpers.IO as io
from word2number import w2n


def writeNum(m, n):
    io.printTTS("Write number from {} to {}".format(m, n))
    for i in range(m, n+1):
        io.printTTS('Write {} in number:'.format(inflect.engine().number_to_words(i)))
        while 1:
            try:
                ans = int(sys.stdin.readline()[:-1])
            except ValueError:
                io.printTTS("input again:")
                continue
            break
            
        if ans == i:
            io.printTTS('Correct')
        else:
            io.printTTS('Wrong')

