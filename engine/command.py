import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takecommand():




    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    try:
       query = takecommand()
       print(query)
       if "open" in query:
          from engine.features import openCommand
          openCommand(query)
       elif "on youtube" :
          from engine.features import playYoutube
          playYoutube(query)
       else:
          print("not run")
    except:
        print("error")
    eel.ShowHood()
    
# old code by sushma
# import pyttsx3
# import speech_recognition as sr
# import eel

# def speak(text):
#     text = str(text)
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices') 
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 174)
    
#     try:
#         eel.DisplayMessage(text)
#         eel.receiverText(text)  # Only call if it exists in JS
#     except AttributeError:
#         pass

#     engine.say(text)
#     engine.runAndWait()

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('listening....')
#         eel.DisplayMessage('listening....')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
        
#         audio = r.listen(source, 10, 6)

#     try:
#         print('recognizing')
#         eel.DisplayMessage('recognizing....')
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said: {query}")
#         eel.DisplayMessage(query)
#     except Exception as e:
#         return ""
    
#     return query.lower()

# @eel.expose
# def allCommands(message=1):
#     query = takecommand()
#     print(query)

#     if "open" in query:
#         from engine.features import openCommand
#         openCommand(query)
#     elif "on youtube" in query:
#         from engine.features import PlayYoutube
#         PlayYoutube(query)
#     else:
#         print("not run")
#         try:
#             eel.ShowHomePage()  # reset UI
#         except AttributeError:
#             pass
