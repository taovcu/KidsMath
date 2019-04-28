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
#from Grade_K.TestCases import TestCases
import Helpers.text2speech as TTS

# Import Packages
import Grade_K.KCC1_3._00_NumberNames as KCC0
import Grade_K.KCC1_3._01_CountTo100By10s as KCC1
import Grade_K.KCC1_3._02_CountfromX as KCC2
import Grade_K.KCC1_3._03_CountTo20 as KCC3
import Grade_K.KCC4_5._04_5_CountToTell as KCC4
import Grade_K.KCC6_7._06_7_CompareNum as KCC6
import Grade_K.KOA1_5._01_5_AlgebraicThink as KOA1
import Grade_K.KNBT1._01_OperationBaseTen as KNBT1
import Grade_K.KMD1_3._01_2_DescribeCompare as KMD1

import Grade_K.BONUS.bonus as Bonus


class Test:
    flag = 0
    def execute(self, func, *args):
        if self.flag:
            return

        if func == 'Number2Name':
            KCC0.Number2Name(args[0])
        if func == 'Name2Number':
            KCC0.Number2Name(args[0])
        if func == 'countNumby10s':
            KCC1.countNumby10s(args[0], args[1])
        if func == 'countNumfromX':
            KCC2.countNumfromX(args[0], args[1])

        if func == 'writeNum':
            KCC3.writeNum(args[0], args[1])
            
        if func == 'countObjects':
            KCC4.countObjects(args[0], args[1])
        if func == 'compareObjects':
            KCC6.compareObjects(args[0], args[1], args[2])
            
        if func == 'compareNum':
            KCC6.compareNum(args[0], args[1])
        if func == 'addTest':
            Bonus.addTest(args[0], args[1])
            
        if func == 'subtractTest':
            Bonus.subtractTest(args[0], args[1])
            
        if func == 'compareItems':
            Bonus.compareItems(args[0], args[1], args[2])
            
        if func == 'guessValue':
            Bonus.guessValue(args[0])
            
        if func == 'AddObjects':
            KOA1.AddObjects(args[0], args[1], args[2])
        if func == 'SubObjects':
            KOA1.SubObjects(args[0], args[1], args[2])
        if func == 'DecomposeNum':
            KOA1.DecomposeNum(args[0], args[1], args[2])
        if func == 'AddupNum':
            KOA1.AddupNum(args[0], args[1], args[2])
            
        if func == 'composeObjBaseTen':
            KNBT1.composeObjBaseTen(args[0], args[1])
        if func == 'composeNumBaseTen':
            KNBT1.composeNumBaseTen(args[0])
        if func == 'decomposeObjBaseTen':
            KNBT1.decomposeObjBaseTen(args[0], args[1])
        if func == 'decomposeNumBaseTen':
            KNBT1.decomposeNumBaseTen(args[0])
            
        if func == 'CompareWeight':
            KMD1.CompareWeight(args[0], args[1])
        if func == 'ClassifyCount':
            KMD1.ClassifyCount(args[0], args[1], args[2], args[3], args[4])

        io.printTTS("Press 'k' to skip current test case; 'q' to quit all tests; any other key to continue")
        i = input()
        if i == 'k':
            self.flag = 1
            return
        elif i == 'q':
            sys.exit()

'''
t = Test()
t.execute('countNumby10s', 100, 1)
t.execute('countNumby10s', 100, 0)
del t

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

KOA1.AddObjects('pear', 3, 4)
KOA1.SubObjects('pear', 13, 4)
KOA1.DecomposeNum('pear', 13, 4)
KOA1.AddupNum('pear', 13, 4)

KNBT1.composeObjBaseTen('pear', 5)
KNBT1.composeNumBaseTen(5)
KNBT1.decomposeObjBaseTen('pear', 15)
KNBT1.decomposeNumBaseTen(15)

KMD1.CompareWeight(20, 40)
KMD1.ClassifyCount('pear', 5, 'grapes', 3, 'orange', 7)
'''
