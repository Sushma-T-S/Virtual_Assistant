import os
import re
import sqlite3
import struct
import time
import webbrowser
# import sqlite3
# import webbrowser
from playsound import playsound
import eel
import pvporcupine
import pyaudio
import pywhatkit as kit
# from engine import hotword
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term
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







#     if not query:
#         speak("Please specify what to open.")
#         return

#     try:
#         # Local system command
#         cursor.execute('SELECT path FROM sys_command WHERE name = ?', (query,))
#         result = cursor.fetchone()
#         if result:
#             speak(f"Opening {query}")
#             os.startfile(result[0])
#             return

#         # Web command
#         cursor.execute('SELECT url FROM web_command WHERE name = ?', (query,))
#         result = cursor.fetchone()
#         if result:
#             speak(f"Opening {query} in the browser")
#             webbrowser.open(result[0])
#             return

#         # Try system fallback
#         speak(f"Trying to open {query}")
#         os.system(f'start {query}')

#     except Exception as e:
#         speak("Something went wrong")
#         print(f"Error: {e}")


# def openCommand(query):
#     query = query.lower()

 

#     # ... rest of your system and web command logic
# # old code by sushma 
# # import os
# # import sqlite3
# # import webbrowser
# # from playsound import playsound
# # import eel
# # from .command import speak
# # from engine.config import ASSISTANT_NAME
# # from engine.helper import extract_yt_term

# # # Connect to database
# # con = sqlite3.connect("jarvis.db")
# # cursor = con.cursor()

# # @eel.expose
# # def playAssistantSound():
# #     music_dir = "www\\assets\\audio\\pop-cartoon-328167.mp3"
# #     playsound(music_dir)

# # def openCommand(query):
# #     query = query.replace(ASSISTANT_NAME, "")
# #     query = query.replace("open", "")
# #     query = query.lower().strip()

# #     if not query:
# #         speak("Please specify what to open.")
# #         return

# #     try:
# #         cursor.execute('SELECT path FROM sys_command WHERE name = ?', (query,))
# #         result = cursor.fetchone()
# #         if result:
# #             speak(f"Opening {query}")
# #             os.startfile(result[0])
# #             return

# #         cursor.execute('SELECT url FROM web_command WHERE name = ?', (query,))
# #         result = cursor.fetchone()
# #         if result:
# #             speak(f"Opening {query} in the browser")
# #             webbrowser.open(result[0])
# #             return

# #         speak(f"Trying to open {query}")
# #         os.system(f'start {query}')

# #     except Exception as e:
# #         speak("Something went wrong")
# #         print(f"Error: {e}")
