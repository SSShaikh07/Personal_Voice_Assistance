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
import pyaudio
import pywhatkit
import pyautogui
import pyjokes
import keyboard
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
from pywikihow import search_wikihow
#from PyDictionary import PyDictionary

def wishMe():
    
    print("Hello Mister Sahil I Am Jarvis")
    speak("Hello Mister Sahil I Am Jarvis")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        print("Good Afternoon Sir") 
        speak("Good Afternoon Sir") 
    else:
        print("Good Evening Sir") 
        speak("Good Evening Sir")    

    print("How may I Help you Sir")
    speak("How may I Help you Sir")



#speak("Say something")
def take_command():
    r=sr.Recognizer()
    m = sr.Microphone()
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
            speak("Say that again sir")

            return "None"
        return Query




def Speak(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    
   
   
    
if __name__=="__main__":
    
    wishMe()
    
    
    
    def music():
        speak("ok sir , Tell me the name of the music. I will play it for you")
        musicName=take_command()
        
        if "Avengers" in musicName:
            os.startfile('E:\\Song\\Avengers.mp3')
            
            
        elif "Tokyo Drift" in musicName:
            os.startfile('E:\\Song\\Tokyo Drift.mp3')  
            
        else:
            pywhatkit.playonyt(musicName)
            speak("Your wish song is not available in my data. I will play it on YouTube")    
            
        speak("Your song has been started. Enjoy Sir")    
    
     
        
    
         
            
    def YouTubeAuto():
        
        speak("What is your YouTube Command!")
        
        comm = take_command()
        
        if 'pause' in comm:
            keyboard.press('space bar')
            speak("Your video has been paused")
            
        elif 'restart' in comm:
            keyboard.press('0')
            speak("Your video has been restart")
            
        elif 'mute' in comm:
            keyboard.press('m')
            speak("Your video has been mute")
        elif 'skip' in comm:
            keyboard.press('l')
            speak("Your video has been skip")
        elif 'back' in comm:
            keyboard.press('j')
            speak("Your video is backed")
             
        elif 'full screen' in comm:
            keyboard.press('f')
            speak("Your video is in full screenff")              
            



    def ChromeAuto():
        speak("please ! Tell me your chrome Automation command")           
        
        comm=take_command()
        
            
        if 'close this tab' in comm:
            keyboard.press_and_release('ctrl  + w')
            speak("Current tab is closed")
            
        elif 'open new tab' in comm:
            keyboard.press_and_release('ctrl  + t')
            speak("new tab is opened")
                    
        elif 'open  new tab in new window' in comm:
            keyboard.press_and_release('ctrl  + n')
            speak("New tab is opened in new window")
            
        elif 'history' in comm:
            keyboard.press_and_release('ctrl  + h') 
            speak("your history is opened")            
            
            
 
    
    while True:
        
        command=take_command()
        speak==Speak(audio)
        if "exit" in command:
            speak("Sure sir as your wish ! bye")
            break
        
        elif "hello" in command:
            speak("Hello Sir! I am Jarvis, Your Personal voice assistant, how may I help you sir...")  
              
         
        elif "how are you Jarvis" in command:
            speak("I'm Fine sir. what's about you")
            
            
        elif "who is Sahil" in command:
            speak("Sahil his full name is sahil shaikh. He is one of the programmer who develop me.")
            speak("Mister sahil is my boss so I call him sir")
            speak("He is student of computer third year")    
            
        
            
        elif "listen" in command:
            speak("Yes I am Listening")
            
        elif "wait" in command:
            speak("Ok sir I am Waiting ")    
             
            
        elif 'Wikipedia' in command:
            speak('Searching Wikipedia...')
            command=command.replace("Wikipedia","")
            results = wikipedia.summary(command,sentences=2)
            speak("According to Wikipedia")
            print("results :")
            speak(results)

        elif "YouTube" in command:
            speak("Sure sir , I will open it on youtube, give me a second")
            command=command.replace("Jarvis","")
            command=command.replace("youtube search" , "")
            webbrowser.open('https://www.youtube.com/results?search_query=' + command)
            speak("Your youtube is opened sir! Thank you")
            
        #elif "YouTube" in command:
        #   speak("Sure sir , I will open the YouTube, give me a second")
        #   webbrowser.open('https://www.youtube.com')    
                

        elif "Google" in command:
            speak("Sure sir , I will open the Google, give me a second")
            webbrowser.open('https://www.google.com/search?gs_ssp=eJzj4tTP1TcwzqtKMzRg9OJMzcnPU8gtLc4GAEjMBtM&q=e' + command)   
            speak("Google is opened sir! Thank you")
        
        elif "python"  in command:
            speak("Sure sir , I will open the python offitial website, give me a second")
            webbrowser.open('http://www.python.org')
            speak("Your python website is opened sir! Thank you")
        elif "Gmail"  in command:
            speak("Sure sir , I will open the Gmail , give me a second")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            speak("Gmail is opened sir! Thank you")
            
        elif "drive"  in command:
            speak("Sure sir , I will open the Google Dive , give me a second")
            webbrowser.open('https://drive.google.com/drive/my-drive')
            speak("Google drive is opened sir! Thank you")            
        
            
        elif 'website' in command:
            speak("Ok sir I will open these website. Give me a second")
            command=command.replace("Jarvis","")
            command=command.replace("website" , "")
            web1 =command.replace("open","") 
            webbrowser.open('https://www.'+web1+".com")    
            
        elif "music" in command:
            music()    
            
           
            
        elif "screenshot" in command:
            ss = pyautogui.screenshot()
            ss.save('D:\\Jarvis Data') 
            


            
    #open a desktop application/software 
     
        elif 'open Chrome' in command:
            speak("Ok sir! I will open chrome,Give me a second")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak("Your command has been completed sir !")
            
        elif 'open vs code' in command:
            speak("Ok sir! I will vs code,Give me a second")
            os.startfile("C:\\Users\Mr Sahil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")        
            speak("Your command has been completed sir !")
                        
        elif 'open pycharm' in command:
            speak("Ok sir! I will open pycharm , Give me a second")
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021\\PyCharm Community Edition 2021.1.1\\bin\pycharm64.exe")        
            speak("Your command has been completed sir !")
            
        elif 'open Instagram' in command:
            speak("Ok sir! I will open Instagram , Give me a second") 
            webbrowser.open('https://www.instagram.com/accounts/login/')
            speak("Your command has been completed sir !")
            
        elif 'open Facebook' in command:
            speak("Ok sir! I will open Facebook,Give me a second")
            webbrowser.open('https://www.facebook.com/')    
            speak("Your command has been completed sir !")
            
        elif 'open WhatsApp' in command:
            speak("Ok sir! I will open Whatsapp,Give me a second")
            webbrowser.open('https://www.whatsapp.com')
            speak("Your command has been completed sir !")
            
        elif 'open telegram' in command:
            speak("Ok sir! I will open telegram,Give me a second")
            webbrowser.open('https://web.telegram.org/k/')   
            speak("Your command has been completed sir !")
            
        elif 'open map' in command:
            speak("Ok sir! I will open google map,Give me a second")
            webbrowser.open('https://www.google.com/maps')
            speak("Your command has been completed sir !")
            
        elif 'open Brave' in command:
            speak("Ok sir! I will open brave browser,Give me a second")
            webbrowser.open('C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe')
            speak("Your command has been completed sir !")
            
            
    #close a desktop apllication/software    
            
        elif 'close vs code' in command:
            speak("Ok sir! I will close vs code,Give me a second")
            os.system("TASKKILL /F /IM Code.exe")
            speak("Your command has been completed sir !")
            speak("vs code has been closed")
            
        elif 'close Chrome' in command:
            speak("Ok sir! I will close chrome,Give me a second")
            os.system("TASKKILL /F /IM chrome.exe")   
            speak("Your command has been completed sir !")
            speak("chrome has been successfully closed")
            
        elif 'close pycharm' in command:
            speak("Ok sir! I will close pycharm,Give me a second") 
            os.system("TASKKILL /F /IM pycharm64.exe") 
            speak("Your command has been completed sir !")
            speak("pycharm has been successfully closed")
            
        elif 'close Instagram' in command:
            speak("Ok sir! I will close Instagram,Give me a second")
            os.system("TASKKILL /F /IM chrome.exe")
            speak("Your command has been completed sir !")
            speak("Instagram has been successfully closed")
            
        elif 'close Facebook' in command:
            speak("Ok sir! I will close Facebook ,Give me a second")       
            os.system("TASKKILL /F /IM chrome.exe")
            speak("Your command has been completed sir !")
            speak("Facebook has been successfully closed")
            
        elif 'close Whatsapp' in command:
            speak("Ok sir! I will close Whatsapp ,Give me a second")       
            os.system("TASKKILL /F /IM chrome.exe")
            speak("Your command has been completed sir !")
            speak("Whatsapp has been successfully closed")
            
        elif 'close telegram' in command:
            speak("Ok sir! I will close telegram ,Give me a second")       
            os.system("TASKKILL /F /IM chrome.exe")
            speak("Your command has been completed sir !")
            speak("telegram has been successfully closed")
            
        elif 'close Map' in command:
            speak("Ok sir! I will close google map ,Give me a second")        
            os.system("TASKKILL /F /IM chrome.exe")             
            speak("Your command has been completed sir !")
            speak("google map has been successfully closed")
            
        
        elif 'close Brave' in command:
            speak("Ok sir! I will close Brave browser ,Give me a second")        
            os.system("TASKKILL /F /IM brave.exe")             
            speak("Your command has been completed sir !")
            speak("Brave browser has been successfully closed")        
            
            
 
        
    #YouTube Commands like pause,full screen,back,restart,etc        
            
        elif 'pause' in command:
            speak("ok sir! I will pause your video")
            keyboard.press('space bar')
            speak("Your video has been paused")

        elif 'restart' in command:
            speak("ok sir! I will restart your video")
            keyboard.press('0')
            speak("Your video has been restart")
            
        elif 'mute' in command:
            speak("ok sir! I will mute your video")
            keyboard.press('m')
            speak("Your video now mute")
           
        elif 'skip' in command:
            speak("ok sir! I will skip these")
            keyboard.press('l')
            speak("Your video is skipped")
         
        elif 'back' in command:
            speak("ok sir! I will play back video")
            keyboard.press('j')
            speak("Now back video is playing")
            
        elif 'full screen' in command:
            speak("ok sir! I will do it")
            keyboard.press('f')
            speak("Your video is in full screen")
         
        elif 'tools' in command:
            YouTubeAuto()    
            speak("YouTube Tools are activated")
  




     
        #chrome Automation command 
        
        elif 'close this tab' in command:
            speak("ok sir! I will close current tab")
            keyboard.press_and_release('ctrl + w')
            speak("Current tab is close")
            
        elif 'open new tab' in command:
            speak("ok sir! I will open new tab")
            keyboard.press_and_release('ctrl + t')
            speak("new tab is opened")
                    
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
            speak("New tab is opened in new window")
            
        elif 'history' in command:
            speak("Ok sir! I will open your chrome history")
            keyboard.press_and_release('ctrl +h') 
            speak("your history is opened")
     
        elif 'tools of chrome' in command:
            ChromeAuto()
            speak("Chrome tools are activated")
        
        #joke in english
        elif "joke" in command:
            get=pyjokes.get_joke()
            speak(get)
            
        elif 'how to' in command:
            Speak("Getting Data From The Internet !")
            op = command.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)      
