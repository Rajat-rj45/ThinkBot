
import datetime
import openai
from config import apikey
import speech_recognition as sr
import os
import win32com.client
import pyaudio
import webbrowser
# import required module
import subprocess, sys
import random
import win32com.client as wincl

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Rajat:{query}\n Jarvis:"
    response = openai.Completion.create(
        # model="gpt-3.5-turbo",
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside of a try catch block
    speaker.speak (response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    # with open(f"Openai/prompt-{random.randint(1,343434343434)}" , "w") as f:
    with open(f"Openai/{' '.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n****************************************\n\n"

    response = openai.Completion.create(
       # model="gpt-3.5-turbo",
        model="text-davinci-003",
        prompt=prompt,

        temperature=0.8,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside of a try catch block
    #  print (response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"Openai/prompt-{random.randint(1,343434343434)}" , "w") as f:
    with open(f"Openai/{' '.join(prompt.split('AI')[1:]).strip()}.txt" , "w") as f:
        f.write(text)


def say(text):
    os.system(f"say {text}")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry from R buddy"


def speak(text):
    speaker = wincl.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

if __name__ == '__main__':
    i=0
    speaker.Speak("Jarvais.. AI")
    while i<=50:
        i=i+1
        print("listening..")
        query= takeCommand()

        # todo: make a list of sites
        sites = [["youtube","https://youtube.com"],["google","https://google.com"],
                 ["Facebook","https://facebook.com"],["linkedin","https://linkedin.com"],
                 ["my portfolio","file:///C:/Users/Abhi/Desktop/Web%20Designing/portfolio/portfolio/index.html"],
                 ["github profile", "https://github.com/Rajat-rj45"], ["instagram profile", "https://www.instagram.com/rajat__ak47/"],
                 ["galgotia college", "https://galgotiacollege.edu/"], ["icloud", "https://gu.icloudems.com/corecampus/index.php"],
                 ["AKTU", "https://aktu.ac.in/syllabus%202023-2024.html"], ["Sarkari result", "https://www.sarkariresult.com/"],
                 ["twitter", "https://twitter.com"], ["flipkart", "https://flipkart.com"],
                 ["Amazon", "https://amazon.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "C:/Users/Abhi/Downloads/rasiya.mp3"
            if os.path.exists(musicPath):
                # Open the music file with the default application
                os.startfile(musicPath)
            else:
                # Speak a message indicating that the file was not found
                speak(f"File not found: {musicPath}")

        if "what is the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strfTime)
            speaker.speak(f"Sir the time is {strfTime}")


        #todo: make a list
        apps=[["camera","C:/Users/Abhi/Desktop/Shortcut/Camera.lnk"],
              ["vs code","C:/Users/Abhi/Desktop/Shortcut/Visual Studio Code.lnk"],
              ["Calculator","C:/Users/Abhi/Desktop/Shortcut/Calculator.lnk"],
              ["Settings","C:/Users/Abhi/Desktop/Shortcut/Settings.lnk"],
              ["Calendar","C:/Users/Abhi/Desktop/Shortcut/Calendar.lnk"],
              ["Games","C:/Users/Abhi/Desktop/Shortcut/Solitaire & Casual Games.lnk"],
              ["Clock", "C:/Users/Abhi/Desktop/Shortcut/Clock.lnk"],
              ["This pc", "C:/Users/Abhi/Desktop/Shortcut/This PC - Shortcut.lnk"],
              ["Mail", "C:/Users/Abhi/Desktop/Shortcut/Mail.lnk"],
              ["Weather", "C:/Users/Abhi/Desktop/Shortcut/Weather.lnk"],
              ["Notepad","C:/Users/Abhi/Desktop/Shortcut/Notepad.lnk"],
              ["WhatsApp","C:/Users/Abhi/Desktop/Shortcut/WhatsApp.lnk"]]

        for app in apps :
            if f"Open {app[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {app[0]} sir...")
                os.startfile(app[1])


        if "Using AI".lower() in query.lower():
            speaker.speak("yes sir")
            ai(prompt=query)

        elif "jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr=""

        else:
            print("Chatting...")
            chat(query)