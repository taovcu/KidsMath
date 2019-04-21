import sys
sys.path.append('../')

# Import Packages
import Grade_K.KCC1_3._00_NumberNames as KCC0
import Grade_K.KCC1_3._01_CountTo100By10s as KCC1
import Grade_K.KCC1_3._02_CountfromX as KCC2
import Grade_K.KCC1_3._03_CountTo20 as KCC3
import Grade_K.BONUS.bonus as Bonus

class TestCasesK:
    testcnt = 0
    # n is user specified number of test cases
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

    
        
