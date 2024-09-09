import os
import speech_recognition as sr
import pyttsx3
import sys

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening.....")
        r.pause_threshold=0.8
        audio=r.listen(source)

    try:
        print("Recognising.....")
        query=r.recognize_google(audio, language='en-in')
        print(f'User said:{query}\n')

    except Exception as e:
        print('Say That Again Please......')
        return "None"
    return query

while True:
    wake_Up = takeCommand().lower()

    if "activate jarvis" in wake_Up:
        print(f"You said:{wake_Up}")
        os.startfile("J.A.R.V.I.S 3.0.pyw")
        speak("Activating Jarvis")
        exit(0)
        
    else:
        print("Nothing.....")
