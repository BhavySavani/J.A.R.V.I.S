from bardapi import BardCookies
import datetime
import re
import webbrowser
import speech_recognition as sr
cookie_dict={
    "__Secure-1PSID":"SECURE-1PSID/FROM/BARDWEBSITE",
    "__Secure-1PSIDTS":"Secure-1PSIDTS/FROM/BARDWEBSITE",
    "__Secure-1PSIDCC":"Secure-1PSIDCC//FROM/BARDWEBSITE",
}

bard=BardCookies(cookie_dict=cookie_dict)

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


def extract_links(text):
  """Extracts website links from a given text string.

  Args:
    text: The text string to extract links from.

  Returns:
    A list of extracted website links.
  """

  pattern = r"https?://[^\s<>\"]+|www\.[^\s<>\"]+"
  links = re.findall(pattern, text)
  return links

while True:
    try:
        query=takeCommand().lower()
        Reply=bard.get_answer(query)['content']
        link=extract_links(Reply)
        webbrowser.open(f"{link[0]}")
    except Exception as e:
        print("Say That Again Please")