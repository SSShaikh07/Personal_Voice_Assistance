from datetime import datetime
from email.mime import audio
from py_compile import main
from turtle import mainloop
from unittest import result
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    speak(" Hello Mister Sahil I Am Jarvis")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir") 
    else:
        speak("Good Evening Sir")    

    speak(" How may I Help you Sir")       


def takeCommand():
    #it take microphone input from the user and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source,duration=1)
        #r.adjust_for_ambient_noise(source, duration=5)
        # r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query =r.recognize.google(audio)
        print("User Said : (query)\n")    

    except Exception as e:
        print(e)

        print("Say that again....")
        return "None"   

    return query     



if __name__ == '__main__':
    #speak("Hii Mister Sahil")
    wishMe()
    while True:
        query = takeCommand().lower()

   
    #logic for instralling task
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print("results :")
            speak(results)

        elif 'open youtube' in query:
             webbrowser.open("youtube.come")

        elif 'open google' in query:
             webbrowser.open("google.come")        

        elif 'open instagram' in query:
             webbrowser.open("instagram.come") 


