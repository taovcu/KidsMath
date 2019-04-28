import sys
sys.path.append('../')

import Helpers.IO as io

def checkEqual(a, b):
    if a == b:
        io.printTTS('Correct')
        return True
    else:
        io.printTTS('Wrong')
        return False

