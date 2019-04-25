import time
import sys
import math
import random
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.CheckAns as ca
import Helpers.IO as io


def CompareWeight(n1, n2):
    io.printTTS("Compare weight of objects")
    io.printTTS("Bob is {} pounds".format(n1))
    pitem.emojiPrint('sheep', 1)
    io.printTTS("Joy is {} pounds".format(n2))
    pitem.emojiPrint('pig2', 1)

    io.printTTS("Who is heavier, Joy or Bob?")
    ans = io.readLine()
    res = ca.checkEqual(ans, 'Joy')
    while not res:
        io.printTTS("Double check")
        ans = io.readLine()
        res = ca.checkEqual(ans, 'Joy')
    io.printTTS("So we know that {} pounds is heavier than {} pounds".format(n1, n2))

    io.printTTS("Who is lighter, Joy or Bob?")
    ans = io.readLine()
    res = ca.checkEqual(ans, 'Bob')
    while not res:
        io.printTTS("Double check")
        ans = io.readLine()
        res = ca.checkEqual(ans, 'Bob')

    io.printTTS("So we know that {} pounds is lighter than {} pounds".format(n2, n1))


def ClassifyCount(m1, n1, m2, n2, m3, n3):
    l = [m1] * n1 + [m2] * n2 + [m3] * n3
    r = random.SystemRandom()
    r.shuffle(l)
    pitem.emojiPrintList(l)
    
    io.printTTS("How many {} do you see?".format(m1))
    ans = io.readInt()
    res = ca.checkEqual(ans, n1)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        res = ca.checkEqual(ans, n1)

    io.printTTS("How many {} do you see?".format(m2))
    ans = io.readInt()
    res = ca.checkEqual(ans, n2)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        res = ca.checkEqual(ans, n2)

    io.printTTS("How many {} do you see?".format(m3))
    ans = io.readInt()
    res = ca.checkEqual(ans, n3)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        res = ca.checkEqual(ans, n3)


