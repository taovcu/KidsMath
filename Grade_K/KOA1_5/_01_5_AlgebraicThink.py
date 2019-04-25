import time
import sys
import math
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.CheckAns as ca
import Helpers.IO as io


def AddObjects(m, n1, n2):
    io.printTTS("Add objects")
    io.printTTS("Bob has {} {}".format(n1, m))
    pitem.emojiPrint(m, n1)
    io.printTTS("Joy has {} {}".format(n2, m))
    pitem.emojiPrint(m, n2)
    io.printTTS("How many {} do they have in total?".format(m))

    ans = io.readInt()
    pitem.emojiPrint(m, ans)
    res = ca.checkEqual(ans, n1 + n2)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        pitem.emojiPrint(m, ans)
        res = ca.checkEqual(ans, n1 + n2)

    io.printTTS("So we know that {} + {} = {}".format(n1, n2, n1 + n2))

def SubObjects(m, n1, n2):
    io.printTTS("Subtract objects")
    io.printTTS("Bob has {} {}".format(n1, m))
    pitem.emojiPrint(m, n1)
    io.printTTS("Joy takes away {} {} from Bob".format(n2, m))
    pitem.emojiPrint(m, n2)
    io.printTTS("How many {} does Bob have now?".format(m))

    ans = io.readInt()
    pitem.emojiPrint(m, ans)
    res = ca.checkEqual(ans, n1 - n2)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        pitem.emojiPrint(m, ans)
        res = ca.checkEqual(ans, n1 - n2)

    io.printTTS("So we know that {} - {} = {}".format(n1, n2, n1 - n2))

def DecomposeNum(m, n, n1):
    io.printTTS("Decompose numbers")
    io.printTTS("We have {} {}".format(n, m))
    pitem.emojiPrint(m, n)
    io.printTTS("We give Joy {} {}".format(n1, m))
    pitem.emojiPrint(m, n1)
    io.printTTS("How many {} are left?".format(m))

    ans = io.readInt()
    pitem.emojiPrint(m, ans)
    res = ca.checkEqual(ans, n - n1)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        pitem.emojiPrint(m, ans)
        res = ca.checkEqual(ans, n - n1)

    io.printTTS("So we know that {} - {} = {}".format(n, n1, n - n1))

def AddupNum(m, n, n1):
    io.printTTS("Add up numbers")
    io.printTTS("Joy has {} {}".format(n1, m))
    pitem.emojiPrint(m, n1)
    io.printTTS("How many more {}s Joy need to buy so she will have {} {}s?".format(m, n, m))

    ans = io.readInt()
    pitem.emojiPrint(m, ans)
    res = ca.checkEqual(ans, n - n1)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        pitem.emojiPrint(m, ans)
        res = ca.checkEqual(ans, n - n1)
    
    io.printTTS("So we know that {} = {} + {}".format(n, n1, n - n1))


