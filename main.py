import speech_recognition as sr
import os
import webbrowser
import datetime
import subprocess
import pyttsx3
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key)

# Initialize text-to-speech engine
engine = pyttsx3.init()


def say(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()


say("Hello, Shreya! Jarvis AI is now active.")

chatStr = ""


def chat(query):
    """Handle chatting using Google Gemini AI."""
    global chatStr
    chatStr += f"User: {query}\nJarvis: "

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        response_text = response.text.strip()
        chatStr += f"{response_text}\n"
        print("AI:", response_text)
        say(response_text)  # Speak response
        return response_text
    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I couldn't process that."


def takeCommand():
    """Listen to user's voice and return as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 4000  # Adjust for background noise
        try:
            audio = r.listen(source, timeout=5)  # Timeout for responsiveness
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return "None"
        except sr.UnknownValueError:
            print("Could not understand.")
            return "None"
        except sr.RequestError:
            print("Could not connect to the internet.")
            return "None"


if __name__ == '__main__':
    print('Welcome to Jarvis AI')
    say("Jarvis AI is ready.")

import os
import webbrowser
import datetime
import subprocess

while True:
    query = takeCommand().lower()
    if query == "none":
        continue  # Skip if no input detected

    # Open common websites
    sites = {
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.com",
        "google": "https://www.google.com"
    }
    for site in sites:
        if f"open {site}" in query:
            say(f"Opening {site}")
            webbrowser.open(sites[site])
            continue

    # Play Music (Update path for Windows)
    if "open music" in query:
        musicPath = r"C:\Users\drart\Downloads\l_theme_death_note.mp3"  # Windows me path change karein
        os.startfile(musicPath)  # Windows me `os.startfile()` use hota hai

    # Time Check
    elif "the time" in query:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        say(f"Sir, the time is {hour} bajke {minute} minutes.")

    # Open Camera (Windows Version)
    elif "open camera" in query:
        subprocess.run("start microsoft.windows.camera:", shell=True)  # Windows Camera command

    # Open Password Manager (Windows me "Passky" ka exact path dalna padega)
    elif "open pass" in query:
        passky_path = r"C:\Path\to\Passky.exe"  # Yahan correct path likhna hoga
        os.startfile(passky_path)

    # AI Chat (Gemini model use hoga)
    elif "using artificial intelligence" in query:
        chat(query)

    # Quit Command
    elif "jarvis quit" in query:
        say("Goodbye, Rey!")
        exit()

    # Reset Chat History
    elif "reset chat" in query:
        chatStr = ""

    else:
        chat(query)  # Default AI model is Gemini


'''import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, how can I help you?")
engine.runAndWait()


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"drart: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

import google.generativeai as genai
genai.configure(api_key)
models = genai.list_models()

for model in models:
    print(model.name)

def chat(query):
    global chatStr
    chatStr += f"User: {query}\n Jarvis: "
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(query)

    # Extract response text
    response_text = response.text.strip()

    print("AI:", response_text)
    return response_text


    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("genai"):
        os.mkdir("genai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"genai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

say("Hello, Rey! Jarvis AI is speaking now.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis AI')
    say("Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/drart/Downloads/l_theme_death_note.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            musicPath = "/Users/drart/Downloads/l_theme_death_note.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open camera".lower() in query.lower():
            os.system(f"open /System/Applications/Camera.app")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
'''
