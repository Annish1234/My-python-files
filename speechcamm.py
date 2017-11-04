#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import smtplib
import os 
import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("choose any one")
    print("camera or mail")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

if  r.recognize_google(audio) == "camera":
                                          cmd="fswebcam -F 3 --fps 20 -r 800x600 cam" + ".jpg"
                                          os.system(cmd)             
elif r.recognize_google(audio) == "mail":
                                            # creates SMTP session
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                            print("Say something to send mail!")
                                            audio = r.listen(source)
                                        try:
                                             # for testing purposes, we're just using the default API key
                                             # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                                             # instead of `r.recognize_google(audio)`
                                            print("You said: " + r.recognize_google(audio))
                                        except sr.UnknownValueError:
                                            print("Google Speech Recognition could not understand audio")
                                        except sr.RequestError as e:
                                            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                                        s = smtplib.SMTP('smtp.gmail.com', 587)
 
                                        # start TLS for security
                                        s.starttls()
                                         
                                        # Authentication
                                        s.login("annishjk01@gmail.com", "krishna@123")
                                         
                                        # message to be sent
                                        message =  r.recognize_google(audio)
                                         
                                        # sending the mail
                                        s.sendmail("annishjk01@gmail.com", "annishjk01@gmail.com", message)
                                         
                                        # terminating the session
                                        s.quit()
