"""
@authors:   Bryan Toscano 'hyde'
            Alicia Ramos
"""

from gtts import *
import vlc
from mutagen.mp3 import MP3

class Text2Speech:
    def __init__(self, script = 'Hello, World', lang = 'en'): #en = English
        self.script = script #like a movie script.  What Ruxpyn is going to read
        self.lang = lang
        self.speed = False #False = fast speed
        self.saveFile = 'Place directory to an output speech file'


#---FUNCTIONS TO SPEAK----------------------------------------------------------------------------------

    def read(self):#says text defined at object creation or default
        speak = gTTS(text = self.script, lang = self.lang, slow = self.speed) #calls google text to speech
        speak.save(self.saveFile) #save file
        player = vlc.MediaPlayer('Place directory to an output speech file')
        player.play() #plays file

    def say(self, script):#says text defined by user
        speak = gTTS(text = script, lang = self.lang, slow = self.speed) #calls google text to speech
        speak.save(self.saveFile) #save file
        player = vlc.MediaPlayer('Place directory to an output speech file')
        player.play() #plays file



#---HELPER FUCNTIONS-------------------------------------------------------------------------------------

    def speed(self, speed): #true for slow, false for false
        self.speed = speed

    def set_script(self, script): #inputs script to read for later
        self.script = script

    def get_script(self):#returns text that is spoken
        return self.script

    def set_lang(self, lang): #set 2 letter language; such as en for english
        self.lang = lang

    def speech_duration(self): #returns duration of speech in seconds
        speech = MP3(self.saveFile)
        duration = speech.info.length
        return duration

