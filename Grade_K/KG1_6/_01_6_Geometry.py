import time
import sys
import math
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.CheckAns as ca
import Helpers.IO as io

import multiprocessing


def IdentifyShape(s):
    io.printTTS("Identify shapes")

    if s in ['circle', 'rectangle', 'square', 'triangle', 'hexagon']:
        p = multiprocessing.Process(target=pitem.plot2D, args=(s,))
    if s in ['cube', 'cone', 'cylinder', 'sphere']:
        p = multiprocessing.Process(target=pitem.plot3D, args=(s,))
    p.start()

    io.printTTS("What is the shape in the picture?")
    ans = io.readLine()
    res = ca.checkEqual(ans, s)
    while not res:
        io.printTTS("Double check")
        ans = io.readLine()
        res = ca.checkEqual(ans, s)

    p.terminate()
