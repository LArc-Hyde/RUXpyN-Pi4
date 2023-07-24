"""
@authors:   Bryan Toscano 'hyde'
            Alicia Ramos
"""
import GSpeech2Text
import GText2Speech 
import chatGPT
import vlc

def main():
    ai = chatGPT.ChatGPT() #creates chatgpt object
    try_to_wake = GSpeech2Text.Speech2Text() #speech2text object
    sound_effects = GText2Speech.Text2Speech()
    woken = False
    while True:
        woken = try_to_wake.wake_PYN() #tries to constantly check for wake word
        if woken == True:
            break #once wake word is found plays sound and starts chat
    player = vlc.MediaPlayer('Place path to a sound file')
    player.play()
    ai.start_chat()

main()
