import sys
sys.path.append('../')

import Helpers.IO as io
import TestConstructor

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
        t = TestConstructor.Test()
        t.execute('Number2Name', 7)
        t.execute('Number2Name', 15)
        t.execute('Number2Name', 22)
        t.execute('Number2Name', 33)
        del t

    def Name2NumberCases(self):
        t = TestConstructor.Test()
        t.execute('Name2Number','three')
        t.execute('Name2Number','seven')
        t.execute('Name2Number','fifteen')
        t.execute('Name2Number','twenty-two')
        del t

    def countNumby10sCases(self):
        t = TestConstructor.Test()
        t.execute('countNumby10s', 100, 1)
        t.execute('countNumby10s', 100, 0)
        del t

    def countNumfromXCases(self):
        t = TestConstructor.Test()
        t.execute('countNumfromX', 3,19)
        t.execute('countNumfromX', 33,51)
        t.execute('countNumfromX', 73,85)
        del t

    def writeNumCases(self):
        t = TestConstructor.Test()
        t.execute('writeNum', 7, 10)
        del t

    def countObjectCases(self):
        t = TestConstructor.Test()
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
        t = TestConstructor.Test()
        t.execute('compareObjects', 'pear', 3, 4)
        t.execute('compareObjects', 'tomato', 7, 9)
        t.execute('compareObjects', 'watermelon', 15, 15)
        del t

    def compareNumCases(self):
        t = TestConstructor.Test()
        t.execute('compareNum', 3, 4)
        t.execute('compareNum', 7, 9)
        t.execute('compareNum', 11, 13)
        t.execute('compareNum', 15, 15)
        del t

    def AddTestCases(self):
        t = TestConstructor.Test()
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
        t = TestConstructor.Test()
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
        t = TestConstructor.Test()
        t.execute('compareItems', 4,6,'cookie')
        t.execute('compareItems', 7,8,'princess')
        t.execute('compareItems', 9,7,'baby')
        t.execute('compareItems', 10,10,'turtle')
        t.execute('compareItems', 13,12,'crocodile')
        del t


    def guessTestCases(self):
        t = TestConstructor.Test()
        t.execute('guessValue', 9)
        t.execute('guessValue', 23)
        t.execute('guessValue', 41)
        t.execute('guessValue', 50)
        del t

    def AddObjectTestCases(self):
        t = TestConstructor.Test()
        t.execute('AddObjects', 'pear', 3, 4)
        del t

    def SubObjectTestCases(self):
        t = TestConstructor.Test()
        t.execute('SubObjects', 'pear', 13, 4)
        del t
    def DecomposeNumTestCases(self):
        t = TestConstructor.Test()
        t.execute('DecomposeNum', 'pear', 13, 4)
        del t
    def AddupNumTestCases(self):
        t = TestConstructor.Test()
        t.execute('AddupNum', 'pear', 13, 4)
        del t
    def composeObjBaseTenTestCases(self):
        t = TestConstructor.Test()
        t.execute('composeObjBaseTen', 'pear', 5)
        del t
    def decomposeObjBaseTenTestCases(self):
        t = TestConstructor.Test()
        t.execute('decomposeObjBaseTen', 'pear', 15)
        del t
    def composeNumBaseTenTestCases(self):
        t = TestConstructor.Test()
        t.execute('composeNumBaseTen', 5)
        del t
    def decomposeNumBaseTenTestCases(self):
        t = TestConstructor.Test()
        t.execute('decomposeNumBaseTen', 15)
        del t
    def CompareWeightTestCases(self):
        t = TestConstructor.Test()
        t.execute('CompareWeight', 20, 40)
        del t
    def ClassifyCountTestCases(self):
        t = TestConstructor.Test()
        t.execute('ClassifyCount', 'pear', 5, 'grapes', 3, 'orange', 7)
        del t

    def IdentifyShapeTestCases(self):
        t = TestConstructor.Test()
        t.execute('IdentifyShape', 'circle')
        t.execute('IdentifyShape', 'rectangle')
        t.execute('IdentifyShape', 'square')
        t.execute('IdentifyShape', 'triangle')
        t.execute('IdentifyShape', 'hexagon')
        t.execute('IdentifyShape', 'cube')
        t.execute('IdentifyShape', 'cone')
        t.execute('IdentifyShape', 'cylinder')
        t.execute('IdentifyShape', 'sphere')
        del t


