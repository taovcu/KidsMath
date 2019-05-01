import sys
import Helpers.text2speech as TTS
import platform
import inflect
import emoji
import settings
from termcolor import colored

def readLine():
    if settings.sttEnable:
        printTTS("Voice input:")
        line = TTS.stt()
        print(line)
        if line and not line['error']:
            t = line['text']
            if t and t.isdigit():
                s = inflect.engine().number_to_words(int(t))
                t = s
    else:
        printTTS("Input from the key board:")
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
    if settings.sttEnable:
        printTTS("Voice input:")
        line = TTS.stt()
        print(line)
        if line and not line['error']:
            t = line['text']
    else:
        printTTS("Input from the key board:")
        t = sys.stdin.readline()[:-1]
    while not t or not t.isdigit():
        printTTS("Input from the key board:")
        t = sys.stdin.readline()[:-1]
    return int(t)

def printTTS(t):
    if settings.zh_cn:
        print(colored(t, 'red') , TTS.en2cn(t))
    else:
        print(colored(t, 'red'))
    #Todo: 'Windows'/'Darwin' TTS
    if settings.ttsEnable:
        if platform.system() in ['Linux', 'Darwin']:
            TTS.tts(t)
