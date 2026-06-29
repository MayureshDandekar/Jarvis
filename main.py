import pyttsx3
import speech_recognition as sr 
import webbrowser 
import music_library
import requests

from dotenv import load_dotenv
import os

load_dotenv()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("Initializing Jarvis")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listneing...")
        r.pauseThreshold = 2

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognising...")
            query = r.recognize_google(audio, language="en-in").lower()
            print(f"You said {query}")
            return query
        except Exception as e:
            speak("Could not understand, please say again")
            return "none"



def openWebsite(query):
    if "youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening youtube")
    elif "google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening google")
    elif "github" in query:
        webbrowser.open("https://www.github.com")
        speak("Opening github")
    else:
        speak("Website not found")



def playMusic(query):
    for song in music_library.music:
        if song in query:
            webbrowser.open(music_library.music[song])
            speak(f"Playing {song}")
            return
    speak("song not found")



def fetchNews():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?language=en&category=technology&apiKey={api_key}"
    response = requests.get(url)
    news = response.json()
    # print(news)
    articles = news["articles"]
    for i, article in enumerate(articles[:5]):
        print(f"{i+1}. {article['title']}")
        speak(article["title"])



while True:
    
    query = takeCommand()
    if "jarvis" in query:
        speak("Yes, how can I help you?")
        command = takeCommand()
        if command != "none":
            if "open" in command:
                openWebsite(command)
            elif "play" in command:
                playMusic(command)
            elif "news" in command:
                fetchNews()
        else :
            speak("I didn't catch that, say Jarvis to try again")



 