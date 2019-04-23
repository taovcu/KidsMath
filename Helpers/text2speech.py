# pip3 install pyttsx3
# pip3 install SpeechRecognition
# apt-get install portaudio19-dev
# pip3 install --upgrade pyaudio


import pyttsx3
import speech_recognition as sr

# text to speech
engine = pyttsx3.init('espeak')
engine.setProperty('rate', 150)
engine.setProperty('voice', 'english-us')

# speech to text
r = sr.Recognizer()
mic = sr.Microphone()


def tts(t):
    engine.say(t)
    engine.runAndWait()

def stt():
    # set up the response object
    response = {
        "error": None,
        "text": None
    }

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
