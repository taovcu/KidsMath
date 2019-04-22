# sudo python -m pip install -U pip
# sudo python -m pip install -U matplotlib
# sudo apt-get install python-tk

# Import Modules
import sys
sys.path.append('.')

import Helpers.IO as io
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import emoji

# Import Packages
from Grade_K.TestCases import TestCases
import Helpers.RemoveSysMethods as RM

sysMethods = ['__class__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


def chooseGrade():
    gradeList = [str(i) for i in range(1,9)]
    gradeList = ['k'] + gradeList
    while 1:
        print("Please choose the Grade of the student:")
        print("    k for Kindergarten")
        print("    [1-8] for Grade 1 to 8")
        grade = io.readChar()
        if grade in gradeList:
            return grade
        else:
            print("Only Grade {} is currently supported".format(gradeList))
            continue

def main():
    print(">>>> Joy Coding Main Function")

    grade = chooseGrade()
    k = TestCases(grade)
    while not k:
        print("Selected Grade {} has not been implemented yet".format(k))
        grade = chooseGrade()
        k = TestCases(grade)

    object_methods = [method_name for method_name in dir(k) 
                      if callable(getattr(k, method_name))]
    RM.RemoveSysMethods(object_methods)

    print("Please specify how many tests you want try:")
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
