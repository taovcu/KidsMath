import sys
import Helpers.text2speech as TTS
import platform

def readChar():
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        return
    while not line:
        readChar()
    return line[0]

def readInt():
    #line = sys.stdin.readline()[:-1]
    printTTS("Please try input the number with you voice:")
    line = TTS.stt()
    print(line)
    if not line['error']:
        t = line['text']
    else:
        printTTS("Please try input the number from the key board:")
        t = sys.stdin.readline()[:-1]

    while not t.isdigit() or line == "":
        printTTS("input is not an int, input again")
        t = sys.stdin.readline()[:-1]
    return int(t)

def printTTS(t):
    print(t)

    #Todo: 'Windows'/'Darwin' TTS
    if platform.system() == 'Linux':
        TTS.tts(t)
