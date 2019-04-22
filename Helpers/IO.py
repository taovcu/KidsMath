import sys
import Helpers.text2speech as TTS

def readChar():
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        return
    while not line:
        readChar()
    return line[0]

def readInt():
    line = sys.stdin.readline()[:-1]
    while not line.isdigit() or line == "":
        print("input is not an int")
        line = sys.stdin.readline()[:-1]
    return int(line)

def printTTS(t):
    print(t)
    TTS.speak(t)
    
