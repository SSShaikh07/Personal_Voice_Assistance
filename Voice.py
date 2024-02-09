from datetime import datetime
from email.mime import audio
from py_compile import main
from turtle import mainloop
from unittest import result
import webbrowser
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email.mime import audio
import speech_recognition as sr
import pyttsx3
from Jarvis import speak




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



#speak("Say something")
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
        
        try:
            print("Recognizing....")
            Query = r.recognize_google(audio)
            print("The query is printed ="+str(Query))
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query





def Speak(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    
    
if __name__=="__main__":
    wishMe()
    while True:
        command=take_command()
        speak==Speak(audio)
        if "exit" in command:
            speak("Sure sir as your wish bye")
            break        
        
        if "insta" in command:
            speak("Best python page on insta is python hub")
            
            
        if "Listen" in command:
            speak("Yes I am Listening")
            
        if "learn" in command:
            speak("Learn python on w3school")
            
        if "code" in command:
            speak("code in vs code")
            
        elif "hello" in command:
            speak("Hello Sir I am Jarvis Your Personal voice assistant how may I help you sir...")
            
            
            
        elif 'Wikipedia' in command:
            speak('Searching Wikipedia...')
            command=command.replace("Wikipedia","")
            results = wikipedia.summary(command,sentences=2)
            speak("According to Wikipedia")
            print("results :")
            speak(results)

        elif "YouTube" in command:
            webbrowser.open('https://www.youtube.com')

        elif "Google" in command:
            webbrowser.open('https://www.google.co.in')   
        
        elif "python"  in command:
            webbrowser.open('http://www.python.org')   
            
                       