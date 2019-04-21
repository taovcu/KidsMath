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
    object_methods = [method_name for method_name in dir(k)                     if callable(getattr(k, method_name))]
    object_methods.remove('__init__')

    # recursively call all the test cases
    for name in object_methods:
        getattr(k, name)()

if __name__ == '__main__':
    main()
