import time
import sys
import math
import inflect
from word2number import w2n

import Helpers.PrintItems as pitem
import Helpers.CheckAns as ca
import Helpers.IO as io

import matplotlib.pyplot as plt

twoDShapes = ['circle', 'rectangle', 'square', 'triangle', 'hexagon']
threeDShapes  = ['cube', 'cone', 'cylinder', 'sphere']

def IdentifyShape(s):
    io.printTTS("Identify shapes")

    if s in twoDShapes:
        fig = pitem.plot2D(s)
    if s in threeDShapes:
        fig = pitem.plot3D(s)
    plt.draw()
    plt.pause(0.5)
    plt.close()

    io.printTTS("What is the shape in the picture?")
    print("hints:")
    print(twoDShapes)
    print(threeDShapes)
    ans = io.readLine()
    res = ca.checkEqual(ans, s)
    while not res:
        io.printTTS("Double check")
        ans = io.readLine()
        res = ca.checkEqual(ans, s)

