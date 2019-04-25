import time
import sys
import math
import inflect
import emoji
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.IO as io

def compareObjects(m, n1, n2):
    io.printTTS("Compare number of objects")
    print(emoji.emojize(':{}: '.format(m) * n1 + ' | ' + ':{}: '.format(m) * n2))
    io.printTTS("Which side has more {}, left or right or same?".format(m))

    ans = io.readLine()
    if (ans == 'same' and n1 == n2) or (ans == 'left' and n1 > n2) or (ans == 'right' and n1 < n2):
        io.printTTS('Correct')
    else:
        io.printTTS('Wrong')

def compareNum(n1, n2):
    io.printTTS("Compare numbers")
    io.printTTS("{} || {} ".format(n1, n2))
    io.printTTS("Which side has greater number, left or right or same?")
    ans = io.readLine()
    if (ans == 'same' and n1 == n2) or (ans == 'left' and n1 > n2) or (ans == 'right' and n1 < n2):
        io.printTTS('Correct')
    else:
        io.printTTS('Wrong')

