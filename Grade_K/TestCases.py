import sys
sys.path.append('../')

import Helpers.IO as io

# Import Packages
import Grade_K.KCC1_3._00_NumberNames as KCC0
import Grade_K.KCC1_3._01_CountTo100By10s as KCC1
import Grade_K.KCC1_3._02_CountfromX as KCC2
import Grade_K.KCC1_3._03_CountTo20 as KCC3
import Grade_K.KCC4_5._04_5_CountToTell as KCC4
import Grade_K.KCC6_7._06_7_CompareNum as KCC6
import Grade_K.BONUS.bonus as Bonus

def TestCases(g):
    if g == 'k':
            return TestCasesK()
    elif g == '1':
            io.printTTS("Grade {} Test Cases have not been created yet".format(g))
            return
    elif g == '2':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return;
    elif g == '3':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return
    elif g == '4':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return
    elif g == '5':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return
    elif g == '6':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return
    elif g == '7':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return
    elif g == '8':
        io.printTTS("Grade {} Test Cases have not been created yet".format(g))
        return
    else:
        io.printTTS("Invalid Grade {}".format(g))
        return

class TestCasesK:
    testcnt = 0
    # n is user specified number of test elif g ==s
    def __init__(self):
        return

    def Number2NameCases(self):
        KCC0.Number2Name(3)
        KCC0.Number2Name(7)
        KCC0.Number2Name(15)
        KCC0.Number2Name(22)
        KCC0.Number2Name(33)


    def Name2NumberCases(self):
        KCC0.Name2Number('three')
        KCC0.Name2Number('seven')
        KCC0.Name2Number('fifteen')
        KCC0.Name2Number('twenty-two')

    def countNumby10sCases(self):
        KCC1.countNumby10s(100, 1)
        KCC1.countNumby10s(100, 0)

    def countNumfromXCases(self):
        KCC2.countNumfromX(3,19)
        KCC2.countNumfromX(33,51)
        KCC2.countNumfromX(73,85)

    def writeNumCases(self):
        KCC3.writeNum(0, 20)

    def countObjectCases(self):
        KCC4.countObjects('pear', 3)
        KCC4.countObjects('apple', 5)
        KCC4.countObjects('gift', 8)
        KCC4.countObjects('tomato', 13)
        KCC4.countObjects('watermelon', 11)
        KCC4.countObjects('corn', 7)
        KCC4.countObjects('banana', 17)
        KCC4.countObjects('grapes', 9)

    def compareObjectCases(self):
        KCC6.compareObjects('pear', 3, 4)
        KCC6.compareObjects('tomato', 7, 9)
        KCC6.compareObjects('grapes', 11, 13)
        KCC6.compareObjects('watermelon', 15, 15)

    def compareNumCases(self):
        KCC6.compareNum(3, 4)
        KCC6.compareNum(7, 9)
        KCC6.compareNum(11, 13)
        KCC6.compareNum(15, 15)

    def AddTestCases(self):
        Bonus.addTest(1, 2)
        Bonus.addTest(2, 2)
        Bonus.addTest(2, 7)
        Bonus.addTest(2, 5)
        Bonus.addTest(3, 6)
        Bonus.addTest(4, 2)
        Bonus.addTest(5, 7)
        Bonus.addTest(6, 3)
        Bonus.addTest(7, 3)
        Bonus.addTest(8, 2)
        Bonus.addTest(8, 7)
        Bonus.addTest(9, 9)
        Bonus.addTest(9, 11)

    
    def subtractTestCases(self):
        Bonus.subtractTest(2, 2)
        Bonus.subtractTest(7, 2)
        Bonus.subtractTest(5, 2)
        Bonus.subtractTest(6, 3)
        Bonus.subtractTest(4, 2)
        Bonus.subtractTest(7, 5)
        Bonus.subtractTest(6, 3)
        Bonus.subtractTest(7, 3)
        Bonus.subtractTest(8, 2)
        Bonus.subtractTest(8, 7)
        Bonus.subtractTest(9, 9)
        Bonus.subtractTest(15, 11)
        Bonus.subtractTest(19, 3)

    
    def compareTestCases(self):
        Bonus.compareItems(4,6,'cookie')
        Bonus.compareItems(7,8,'princess')
        Bonus.compareItems(9,7,'baby')
        Bonus.compareItems(10,10,'turtle')
        Bonus.compareItems(13,12,'crocodile')


    def guessTestCases(self):
        Bonus.guessValue(9)
        Bonus.guessValue(23)
        Bonus.guessValue(41)
        Bonus.guessValue(50)

