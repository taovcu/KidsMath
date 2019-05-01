import sys
sys.path.append('.')

import Helpers.IO as io
import random
import emoji

from Grade_K.TestCases import TestCases
import Helpers.Control as CTR


def chooseGrade():
    gradeList = [str(i) for i in range(1,9)]
    gradeList = ['k'] + gradeList
    while 1:
        io.printTTS('Please choose the Grade of the student:')

        io.printTTS("    k for Kindergarten")
        io.printTTS("    [1-8] for Grade 1 to 8")
        grade = io.readChar()
        if grade in gradeList:
            return grade
        else:
            io.printTTS("Only Grade {} is currently supported".format(gradeList))
            continue


"""
This is the main function of the project
"""
def main():
    print(">>>> Welcome to KidsMath, Enjoy! <<<<")

    grade = chooseGrade()
    k = TestCases(grade)
    while not k:
        io.printTTS("Selected Grade {} has not been implemented yet".format(k))
        grade = chooseGrade()
        k = TestCases(grade)

    object_methods = [method_name for method_name in dir(k)
                      if callable(getattr(k, method_name))]
    object_methods = CTR.RemoveSysMethods(object_methods)

    io.printTTS("There are totally {} test cases implemented".format(len(object_methods)))

    io.printTTS("Please specify how many tests you want try:")
    testcnt = io.readInt()

    RandomMethodList = []
    for i in range(testcnt):
       secure_random = random.SystemRandom()
       m = secure_random.choice(object_methods)
       RandomMethodList.append(m)
       object_methods.remove(m)

    print(RandomMethodList)
    # recursively call all the test cases
    for name in RandomMethodList:
        getattr(k, name)()


if __name__ == '__main__':
    main()
