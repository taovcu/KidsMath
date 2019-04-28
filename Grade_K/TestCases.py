import sys
sys.path.append('../')

import Helpers.IO as io
import Helpers.Control as CTR
import test

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
        t = test.Test()
        t.execute('Number2Name', 7)
        t.execute('Number2Name', 15)
        t.execute('Number2Name', 22)
        t.execute('Number2Name', 33)
        del t

    def Name2NumberCases(self):
        t = test.Test()
        t.execute('Name2Number','three')
        t.execute('Name2Number','seven')
        t.execute('Name2Number','fifteen')
        t.execute('Name2Number','twenty-two')
        del t

    def countNumby10sCases(self):
        t = test.Test()
        t.execute('countNumby10s', 100, 1)
        t.execute('countNumby10s', 100, 0)
        del t

    def countNumfromXCases(self):
        t = test.Test()
        t.execute('countNumfromX', 3,19)
        t.execute('countNumfromX', 33,51)
        t.execute('countNumfromX', 73,85)
        del t

    def writeNumCases(self):
        t = test.Test()
        t.execute('writeNum', 7, 10)
        del t

    def countObjectCases(self):
        t = test.Test()
        t.execute('countObjects', 'pear', 3)
        t.execute('countObjects', 'palm_tree', 5)
        t.execute('countObjects', 'tulip', 8)
        t.execute('countObjects', 'tomato', 13)
        t.execute('countObjects', 'watermelon', 11)
        t.execute('countObjects', 'sunflower', 7)
        t.execute('countObjects', 'banana', 17)
        t.execute('countObjects', 'grapes', 9)
        del t

    def compareObjectCases(self):
        t = test.Test()
        t.execute('compareObjects', 'pear', 3, 4)
        t.execute('compareObjects', 'tomato', 7, 9)
        t.execute('compareObjects', 'watermelon', 15, 15)
        del t

    def compareNumCases(self):
        t = test.Test()
        t.execute('compareNum', 3, 4)
        t.execute('compareNum', 7, 9)
        t.execute('compareNum', 11, 13)
        t.execute('compareNum', 15, 15)
        del t

    def AddTestCases(self):
        t = test.Test()
        t.execute('addTest', 1, 2)
        t.execute('addTest', 2, 2)
        t.execute('addTest', 2, 7)
        t.execute('addTest', 3, 6)
        t.execute('addTest', 4, 2)
        t.execute('addTest', 5, 7)
        t.execute('addTest', 6, 3)
        t.execute('addTest', 7, 3)
        t.execute('addTest', 8, 2)
        t.execute('addTest', 8, 7)
        t.execute('addTest', 9, 9)
        t.execute('addTest', 9, 11)
        del t

    
    def subtractTestCases(self):
        t.execute('subtractTest', 2, 2)
        t.execute('subtractTest', 7, 2)
        t.execute('subtractTest', 6, 3)
        t.execute('subtractTest', 7, 3)
        t.execute('subtractTest', 8, 2)
        t.execute('subtractTest', 9, 9)
        t.execute('subtractTest', 15, 11)
        t.execute('subtractTest', 19, 3)
        del t

    
    def compareTestCases(self):
        t.execute('compareItems', 4,6,'cookie')
        t.execute('compareItems', 7,8,'princess')
        t.execute('compareItems', 9,7,'baby')
        t.execute('compareItems', 10,10,'turtle')
        t.execute('compareItems', 13,12,'crocodile')
        del t


    def guessTestCases(self):
        t.execute('guessValue', 9)
        t.execute('guessValue', 23)
        t.execute('guessValue', 41)
        t.execute('guessValue', 50)
        del t

