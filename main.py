
from asyncore import write
import datetime
import os
import smtplib
import webbrowser
from ast import Pass
from winsound import PlaySound
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import numpy
 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")  

    speak("hey this is me Aman how may i help you please tell you want write or speak")
    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kashyapdhruv86@gmail.com', 'vtjcvugtubapwkbf')
    server.sendmail('kashyapdhruv86@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    i=str(input("enter speak or write"))
    
    while True:
        if 'write' in i :
            speak("please write any command")
            query=str(input("enter you want to say"))
        else:
            speak("ok i am listening please speak")
            query = takeCommand().lower()
        if 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'tell me' in query:
            speak('Searching on web about your query...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'who' in query:
            speak('Searching on web about your query...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'when' in query:
            speak('Searching on web about your query...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'what' in query:
            speak('Searching on web about your query...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak("sir do you want to listen music from you tube")
            if "write" in i.lower():
                v=str(input("enter yes or no"))
            else:
                v = takeCommand().lower()
            if "yes" in v.lower():
                speak("tell me which song would you like to listen")
                if "write" in i.lower():
                    k=str(input("enter song"))
                else:
                    k=takeCommand().lower()
                pywhatkit.playonyt(k)
            #else:
             #   music_dir = ''                     #song directory ka naam
             #   songs = os.listdir(music_dir)
             #   print(songs)    
             #   os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ""                        #yaha vscode add
            os.startfile(codePath)

        elif 'email to christopher' in query:
            try:
                speak("What should I say?")
                if "write" in i:
                    content=str(input("enter what you wnat to send"))
                else:
                    content = takeCommand()
                to = "kahyapdhruv86@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'thanks emmit' in query:
            speak("welcome sir")
            break
        elif 'how are you' in query:
            speak("i am good sir how are you")
        else:
            if "write" in i:
                speak("sir can you write that again")
            else:
                speak("sir can you say that again ")
