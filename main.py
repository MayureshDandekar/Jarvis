import pyttsx3
import speech_recognition as sr  

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Initializing Jarvis")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listneing...")
        r.pauseThreshold = 1

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said {query}")
            return query
        except Exception as e:
            print("Could not understand, please say again")
            return "none"

takeCommand()








