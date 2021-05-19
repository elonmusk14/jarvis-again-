import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import random
import pyjokes
from pywikihow import search_wikihow 
from bs4 import BeautifulSoup
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morniing sir")

    elif hour>= 12 and hour < 18:
        speak("Good afternoon sir ")

    else: speak("Good evening sir")

    speak("Please tell me how may i help you")

def Takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognising...')
            quary = r.recognize_google(audio, language='en-US')
            if "jarvis" in quary:
                quary = quary.replace("jarvis", "")
            print(quary)

        except Exception as e:
            print('Say that again please...')
            return "None"
        return quary

if __name__ == '__main__':
         
    wishMe()
    while True:
            
        query = Takecommand().lower() 

        query = query.replace("jarvis", "")
                
            # Logic for executing task based on query
                
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open('google.com')            

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open('https://stackoverflow.com/')            

        elif 'open w3schools' in query:
            speak("opening w3schools")
            webbrowser.open('w3schools.com')            

        elif 'open 10fastfingers' in query:
            speak("opening ")
            webbrowser.open('10fastfingers.com')            

        elif 'open amazon' in query:
            webbrowser.open('amazon.com')  
                        
        elif 'open classroom' in query:
            webbrowser.open('classroom.google.com')

        elif  'music' in query:
            speak("I am playing some random music for you")
            music_dir = 'D:\\songs'                                       # MODIFY PART
            songs = os.listdir(music_dir)
            ran = random.randint(0, len(songs))
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[ran]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"sir the current time is {strTime}")

        elif 'open visual studio code' in query:      # jarvis will ask that you want vs code or pycharm
            speak("opening visual studio code")
            codepath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   # MODIFY PART
            os.startfile(codepath)

        elif 'open pycharm' in query:      # jarvis will ask that you want vs code or pycharm
            speak("opening pycharm ")
            codes =  "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"  # MODIFY PART
            os.startfile(codes)

        elif 'close' in query:
            speak("shutting down..")
            break

        elif "tell me a joke" in query:
            a = pyjokes.get_joke()
            speak(a)
            print(a)
               
        elif "are you there" in query:
            speak("That's my service sir    ")

        elif 'play' in query:
            speak(f"playing {query}")
            query = query.replace("play","")                # Playing video in youtube
            pywhatkit.playonyt(query)
                
        elif 'temperature' in query:
            search = "temperature in raipur chhattisgarh"
            url = f"http://www.google.com/search?q={search}"         
            r = requests.get(url)                                       # Not completed 
            data = BeautifulSoup(r.text,'html.parser')
            temp = data.find("div",class_ = "BNeawe").txt
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")
                
        elif "how to" in query:
            max_result = 1
            how_to = search_wikihow(query,max_result)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)
                
                               
        if "who is" in query:
            try:
                person = query.replace("who is","")
                speak(f"searching {query}")
                info = wikipedia.summary(person,2)
                print(info)
                speak(info)
            except Exception as e:
                    print(e)