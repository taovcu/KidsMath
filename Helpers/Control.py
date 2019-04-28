import sys
sys.path.append('../')

import Helpers.IO as io

def quitProgram():
    io.printTTS("Press ")
    i = input()
    if i == 'q':
        sys.exit()

def RemoveSysMethods(obj):
    obj_2 = [i for i in obj if i[:2] != '__']
    return obj_2
