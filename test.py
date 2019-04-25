import sys
sys.path.append('.')


import Helpers.IO as io
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import emoji
import pyttsx3

# Import Packages
from Grade_K.TestCases import TestCases
import Helpers.RemoveSysMethods as RM
import Helpers.text2speech as TTS

# Import Packages
import Grade_K.KCC1_3._00_NumberNames as KCC0
import Grade_K.KCC1_3._01_CountTo100By10s as KCC1
import Grade_K.KCC1_3._02_CountfromX as KCC2
import Grade_K.KCC1_3._03_CountTo20 as KCC3
import Grade_K.KCC4_5._04_5_CountToTell as KCC4
import Grade_K.KCC6_7._06_7_CompareNum as KCC6
import Grade_K.KOA1_5._01_5_AlgebraicThink as KOA1
import Grade_K.BONUS.bonus as Bonus

'''
KCC0.Number2Name(3)
KCC0.Number2Name(7)

KCC0.Name2Number('seven')
KCC0.Name2Number('fifteen')

KCC1.countNumby10s(100, 1)
KCC1.countNumby10s(100, 0)

KCC2.countNumfromX(3,19)
KCC2.countNumfromX(33,51)

KCC3.writeNum(0, 20)

KCC4.countObjects('gift', 8)
KCC4.countObjects('tomato', 13)
KCC6.compareObjects('tomato', 7, 9)
KCC6.compareObjects('grapes', 11, 13)

KCC6.compareNum(7, 9)
KCC6.compareNum(11, 13)
Bonus.addTest(4, 2)
Bonus.addTest(5, 7)

Bonus.subtractTest(6, 3)
Bonus.subtractTest(7, 3)

Bonus.compareItems(7,8,'princess')
Bonus.compareItems(9,7,'baby')

Bonus.guessValue(23)
Bonus.guessValue(41)
'''

KOA1.AddObjects('pear', 3, 4)
KOA1.SubObjects('pear', 13, 4)
KOA1.DecomposeNum('pear', 13, 4)
KOA1.AddupNum('pear', 13, 4)
