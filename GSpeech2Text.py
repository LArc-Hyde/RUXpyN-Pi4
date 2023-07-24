"""
@authors:   Bryan Toscano 'hyde'
            Alicia Ramos
"""

import GText2Speech
import speech_recognition as sr
from speech_recognition import exceptions as ex
ex.UnknownValueError

class Speech2Text:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.text = 'Nothing Yet'
        self.errorResponse = GText2Speech.Text2Speech()


#---FUNCTIONS CAPTURING SPEECH--------------------------
    
    def capture(self):
        with sr.Microphone() as source:
            while True:
                try:
                    speech = self.recognizer.record(source, duration = 5)#duration refers to how long it will wait before next RuxPyn action.
                    print('Recognizing standard...')
                    text = self.recognizer.recognize_google(speech)
                    break
                except ex.UnknownValueError: #forces chatgpt to ask for input when it doesn't understand the user
                    print("UnkownValueError")
                    self.say_err()
            self.text = text
            return text
    
    #function that keeps ruxpyn listening
    def capture_noisy(self):
        with sr.Microphone() as source:
            while True:
                try:
                    self.recognizer.adjust_for_ambient_noise(source, duration = 2)# duration wait to process background noise 
                    print('Recognizing noisy...')
                    speech = self.recognizer.listen(source, timeout = None)#note there is no timeout set for the listen
                    text = self.recognizer.recognize_google(speech)
                    break
                except ex.UnknownValueError:#forces chatgpt to ask for input when it doesn't understand the user
                    print("UnkownValueError")
                    self.say_err()
            self.text = text 
            return text
    
    #function for confirmation that wake work is acknowledged
    def wake_PYN(self):
        with sr.Microphone() as source:
            while True:
                try: 
                    self.recognizer.adjust_for_ambient_noise(source, duration = 0.2)# duration wait to process background noise
                    print('Recognizing wake...')
                    speech = self.recognizer.listen(source)

                    #wake will be used to check wake word
                    wake = self.recognizer.recognize_google(speech)
                    break
                except ex.UnknownValueError:#forces chatgpt to ask for input when it doesn't understand the user
                    print("UnkownValueError")
                    self.say_err()
            #wake word is set
            wake = wake.lower()

            if 'hey pin' in wake:#the wake word can be changed to whatever the user wants
                return True
                
            else:
                return False
                

#---Helper Functions-------------------------------------

    def dur(self, duration):
        self.times = duration

    def get_text(self):
        return self.text()

    def say_err(self):
        self.errorResponse.say('I did not quite get that.  Can you say that again?')

