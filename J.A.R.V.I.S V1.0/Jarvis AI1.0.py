import pyttsx3
import datetime
import os
import speech_recognition as sr
import wikipedia
from googlesearch import search
import webbrowser
import pyautogui


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")
    
    speak("Allow   me   to    Introduce    Myself.  I    am    jarvis,      The    virtual    Artificial   intelligence and  I   am   here   to   assist you to variety of tasks as best I can,  24 hours a day 7 days a week. Importing your prefrences from home interface. System is now fully operational. Tell me how may I help you?")

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



if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences = 2)
            speak("According To wikipedia")
            print (results)
            speak (results)

        elif "open google" in query:
            speak("Opening Google.....")
            print("Opening Google...")
            webbrowser.open(f"https://www.google.com")

        elif "search google" in query:
            speak("Searching On Google.....")
            print("Searching On Google.....")
            query=query.replace("search google","")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'open youtube' in query:
            speak("Opening Youtube.....")
            print("Opening Youtube.....")
            query=query.replace("search youtube",'')
            webbrowser.open('www.youtube.com')

        elif 'search youtube' in query:
            speak("Searching Youtube.....")
            print("Searching Youtube.....")
            query=query.replace("search youtube",'')
            webbrowser.open(f'www.youtube.com/results?search_query={query}')
            
        elif 'stack overflow' in query:
            speak("Opening Stackoverflow.com.....")
            speak("Opening Stackoverflow.com.....")
            webbrowser.open('www.stackoverflow.com')

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir The Time is {strTime}')
            print(strTime)

        elif 'open code' in query:
            speak("Opening VS Code.....")
            print("Opening VS Code.....")
            os.startfile("/location/to/CodeEditor")

        elif 'open minecraft' in query:
            speak("Opening Minecraft.....")
            print("Opening Minecraft.....")
            os.startfile("/location/to/Minecraft")

        elif 'open velo' in query:
            speak("Opening Valorant.....")
            print("Opening Valorant.....")
            os.startfile("/location/to/Valorant")
            
        elif '.com' in query:
            speak(f"Opening {query}.....")
            print(f"Opening {query}.....")
            query=query.replace(".com",'')
            webbrowser.open(f"www.{query}.com")

        elif 'screenshot' in query:
            i = 1
            if i>0:
                i+=1
                ss= pyautogui.screenshot()
                ss.save(f'/location/to/save/screenshots')
                speak("Screenshot Saved To Your Folder")
        elif 'shutdown pc' in query:
            os.system("shutdown /s /t 1")
            speak("shutting down pc")
            exit()
        
        elif 'exit' in query:
            os.startfile('Wake Up Console.pyw')
            speak("Quitting")
            exit()

        elif'open the' in query:
            query=query.replace("open the","")
            os.startfile(f'location/to/common/folders/of/applications/')
            speak(f"Opening {query}")


