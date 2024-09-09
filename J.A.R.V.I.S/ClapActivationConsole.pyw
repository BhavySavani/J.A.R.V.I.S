import sounddevice as sd
import numpy as np
import os
import pyttsx3
import sys


def speak(audio):
    subprocess.call(["say",audio])
Clap=False
threshold=25

def detect_clap(indata,frames,time,status):
    global Clap
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm>threshold:
        print("Clap Detected!")
        Clap=True

def Listen_for_Claps():
    with sd.InputStream(callback=detect_clap):
        return sd.sleep(1000)

if __name__ == "__main__":
    while True:
        Listen_for_Claps()
        print("Listening.")
        if Clap==True:
            os.startfile("J.A.R.V.I.S 3.0.pyw")
            speak("Activating Jarvis")
            exit()
        else:
            pass
