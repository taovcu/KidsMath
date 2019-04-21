# sudo python -m pip install -U pip
# sudo python -m pip install -U matplotlib
# sudo apt-get install python-tk

# Import Modules
import sys
sys.path.append('.')

import time
import matplotlib.pyplot as plt
import numpy as np
import emoji

# Import Packages
from Grade_K.TestCases import TestCases


def main():
    print(">>>> Joy Coding Main Function")
    k = TestCases(3)
    k.AddTestCases()
    k.writeNumCases()

    #KCC0.Number2Name(3)
    #KCC1.countNumby10s(40, 1)
    #KCC2.countNumfromX(3, 5)
    #KCC3.countNum(5, 11)

if __name__ == '__main__':
    main()
