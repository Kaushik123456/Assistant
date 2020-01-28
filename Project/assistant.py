import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import numpy as np


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<=23:
        speak("Good Evening Sir!")
    
    speak("I am your assistant. How can i help you Sir ?")

def takecommand():

    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing!")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Say again")
        speak("Sorry! , Say again")
        takecommand()
        return "None"
    return query

if __name__ == "__main__":
    welcome()
    while True:
        speak("Please say your command!!")
        command = takecommand().lower()
        
        # Logic for executing tasks based on command
        if 'tell' in command:
            speak("Gathering Please wait.....!!!")
            command = command.replace("search", "")
            res = wikipedia.summary(command,sentences=3)
            print("According to wikipedia",res)
            speak("According to wikipedia ")
            speak(res)
        elif 'search' in command:
            query = " "
            for i in command.split(" "):
                if(i != "search"):
                    query += i+" " 
            webbrowser.open("https://www.google.com/search?q="+query)
            speak("This what i had found on web!!!")
        elif 'youtube' in command:
            speak("Do you want to open youtube or search any video")
            speak("If you want to open only youtube then say skip")
            speak("If you want search any video then say video and your input")
            command = takecommand().lower()
            query = " "
            if(command == "skip"):
                webbrowser.open("https://www.youtube.com")
            else:
                for i in command.split(" "):
                    if(i != "video"):
                        query += i+" "
                webbrowser.open("https://www.youtube.com/results?search_query="+query)
            speak("Opening Youtube")
        elif 'facebook' in command:
            webbrowser.open("https://www.facebook.com/")
            speak("Opening facebook")
        elif 'date' in command:
            res = datetime.datetime.now().date()
            print("Now date is : ",res)
            speak("Now date is :")
            speak(res)
        elif 'time' in command:
            res = datetime.datetime.now().strftime("%H:%M:%S")
            print("Now time is : ",res)
            speak("Now time is :")
            speak(res)
        elif 'exit' or 'quit' in command:
            speak("exiting, Bye Now!!")
            exit()