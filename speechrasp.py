#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=5)
    print("Say something!")
    while True:
        audio = r.listen(source) 
        print("You said: " + r.recognize_google(audio))
