from playsound import playsound
import eel

#playing assistant sound function
@eel.expose

#playing assistant function
def playAssistantSound():
    music_dir = "www\\assets\\audio\\pop-cartoon-328167.mp3"
    playsound(music_dir)