from winsound import PlaySound
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
from gtts import tts
def save(filename):
    filename.save()
    

#BU OLDUUUUU


def speak(string):
   
    # playsound("Olive.mp3")
    file="cevap.mp3"
    save(file)
    playsound(file)
    # os.remove(file)

speak("merhaba bilgisiyar açıldı")

speak("hello")