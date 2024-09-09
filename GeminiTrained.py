import re
import google.generativeai as genai
import os
import webbrowser
import pyttsx3

genai.configure(api_key="APIKeyHERE")

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
    
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "Hey Jarvis"
  },
  {
    "role": "model",
    "parts": "Hello Sir! How may I help you today?"
  },
  {
    "role": "user",
    "parts": "Can You Open Chrome for me"
  },
  {
    "role": "model",
    "parts": "Certainly! Opening Google Chrome for you now.\n\n*Google Chrome opens up on your screen*\n\nIs there anything else I can assist you with today?"
  },
  {
    "role": "user",
    "parts": "can you open youutbe.com for me<div><br></div>"
  },
  {
    "role": "model",
    "parts": "Absolutely! Opening YouTube for you now.<br>"
  },
  {
    "role": "user",
    "parts": "Open Youtube video for Starship IFT-2"
  },
  {
    "role": "model",
    "parts": "Sure, here's the YouTube video for Starship IFT-2, as requested:\n\n*https://www.youtube.com/watch?v=M10-aR6zSWQ*\n\nLet me know if there's anything else I can help you with today!"
  },
  {
    "role": "user",
    "parts": "Hey JArvis how are you?"
  },
  {
    "role": "model",
    "parts": "I am doing very well, thank you for asking. I am always here to help you with anything you may need. Is there anything specific I can assist you with today?"
  },
  {
    "role": "user",
    "parts": "open youutbe video of linus tech tips give me the link"
  },
  {
    "role": "model",
    "parts": "Here is the link to the latest Linus Tech Tips video on YouTube:\n\nhttps://youtu.be/siPpOwrorm4?si=9Paei4cZdcxbbR4G\n\nThis video is titled \"Breaking the RTX 4090 in Half... Literally\" and was uploaded on November 8, 2022.\n\nWould you like me to open this video in your default web browser?"
  },
])
query=input("ENter:")
reply=convo.send_message(f"{query}")
'''Reply=re.sub(r"\*[^\*]*\*", "", reply)'''
print(reply)
#speak(Reply)
#link=extract_links(reply)
#print(link)
try:
  if "opening google chrome" in reply:
    os.startfile(f"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
  elif links != []:
    webbrowser.open(f"{links[0]}")
except Exception as e:
  speak("Error!")
