import sys
import Helpers.text2speech as TTS
import platform
import inflect

def readLine():
    printTTS("Voice input:")
    line = TTS.stt()
    print(line)
    if line and not line['error']:
        t = line['text']
        if t and t.isdigit():
            s = inflect.engine().number_to_words(int(t))
            t = s
    else:
        printTTS("Cannot recognize what you said. Input from the key board:")
        t = sys.stdin.readline()[:-1]
        while not t:
            printTTS("Input from the key board:")
            t = sys.stdin.readline()[:-1]
    return t

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
    printTTS("Voice input:")
    line = TTS.stt()
    print(line)
    if line and not line['error']:
        t = line['text']
    else:
        printTTS("Input from the key board:")
        t = sys.stdin.readline()[:-1]
        while not t.isdigit() or t == "":
            printTTS("Input from the key board:")
            t = sys.stdin.readline()[:-1]
    return int(t)

def printTTS(t):
    print(t)
    #Todo: 'Windows'/'Darwin' TTS
    if platform.system() in ['Linux', 'Darwin']:
        print(TTS.en2cn(t))
        TTS.tts(t)
