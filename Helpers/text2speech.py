import pyttsx3

engine = pyttsx3.init('espeak')
engine.setProperty('rate', 150)
engine.setProperty('voice', 'english-us')

def speak(t):
    engine.say(t)
    engine.runAndWait()
    
