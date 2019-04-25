import time
import sys
import math
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.CheckAns as ca
import Helpers.IO as io


def composeObjBaseTen(m, n):
    io.printTTS("Add objects based on 10")
    io.printTTS("Bob has 10 {}s".format(m))
    pitem.emojiPrint(m, 10)
    io.printTTS("Joy gives Bob {} more {}s".format(n, m))
    pitem.emojiPrint(m, n)
    io.printTTS("How many {}s does Bob have now?".format(m))

    ans = io.readInt()
    pitem.emojiPrint(m, ans)
    res = ca.checkEqual(ans, n + 10)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        pitem.emojiPrint(m, ans)
        res = ca.checkEqual(ans, n + 10)

    io.printTTS("So we know that {} = {} + {}".format(10 + n, 10, n))


def composeNumBaseTen(n):
    io.printTTS("Add numbers based on 10")
    io.printTTS("10 + {} = ".format(n))

    ans = io.readInt()
    res = ca.checkEqual(ans, n + 10)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        res = ca.checkEqual(ans, n + 10)

    io.printTTS("So we know that {} = {} + {}".format(10 + n, 10, n))


def decomposeObjBaseTen(m, n):
    io.printTTS("Take 10 objects away")
    io.printTTS("Bob has {} {}s".format(n, m))
    pitem.emojiPrint(m, n)
    io.printTTS("Joy takes 10 {}s away".format(m))
    pitem.emojiPrint(m, 10)
    io.printTTS("How many {}s does Bob have now?".format(m))

    ans = io.readInt()
    pitem.emojiPrint(m, ans)
    res = ca.checkEqual(ans, n - 10)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        pitem.emojiPrint(m, ans)
        res = ca.checkEqual(ans, n - 10)

    io.printTTS("So we know that {} = {} - {}".format(n - 10, n, 10))

def decomposeNumBaseTen(n):
    io.printTTS("Subtract 10")
    io.printTTS("{} - 10 = ".format(n))

    ans = io.readInt()
    res = ca.checkEqual(ans, n - 10)
    while not res:
        io.printTTS("Double check")
        ans = io.readInt()
        res = ca.checkEqual(ans, n - 10)

    io.printTTS("So we know that {} = {} - {}".format(n - 10, n, 10))

