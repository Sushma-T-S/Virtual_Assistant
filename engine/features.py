import os
import re
from shlex import quote
import sqlite3
import struct
import subprocess
import time
import webbrowser
# import sqlite3
# import webbrowser
from playsound import playsound
import eel
import pvporcupine
import pyaudio
import pyautogui
import pywhatkit as kit
# from engine import hotword
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term, remove_words
# from engine.helper import extract_yt_term  # Make sure path is correct

# # Rename your local function
# def start_hotword_detection():
#     print("Hotword detection started")

# # Connect to database
con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\pop-cartoon-328167.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()
    if app_name !="":
        try:
           cursor.execute(
               'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
           results = cursor.fetchall()

           if len(results) != 0:
               speak("Opening " + query)
               webbrowser.open(results[0][0])
           else:
               speak("Opening " + query)
               try:
                   os.system('start ' + query)
               except:
                   speak("not found")
        except:
            speak("something went wrong")


def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing "+search_term+"on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        #pre trained keyword
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        #loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            #processing keyword comes from mic
            keyword_index=porcupine.process(keyword)
            #checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                #pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

import time
import subprocess
import pyautogui
from urllib.parse import quote

def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        jarvis_message = "Message sent successfully to " + name
    elif flag == 'call':
        message = ''
        jarvis_message = "Calling " + name
    elif flag == 'video call':
        message = ''
        jarvis_message = "Starting video call with " + name

    # Encode and prepare WhatsApp link
    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Launch WhatsApp Desktop
    subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
    time.sleep(5)  # Ensure the app is open

    # Depending on the call type, click the correct icon
    if flag == 'message':
        pyautogui.press('enter')  # Send message
    elif flag == 'call':
        time.sleep(2)  # Wait for chat to open
        pyautogui.click(1265, 100)  # Click on the voice call button (use correct coordinates)
    elif flag == 'video call':
        time.sleep(2)  # Wait for chat to open
        pyautogui.click(1210, 100)  # Click on the video call button (use correct coordinates)

    time.sleep(1)  # Wait for the action to complete
    speak(jarvis_message)