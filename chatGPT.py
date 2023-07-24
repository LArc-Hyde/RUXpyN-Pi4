"""
@authors:   Bryan Toscano 'hyde'
            Alicia Ramos
"""

import openai
import GText2Speech
import speech_recognition as sr
import GSpeech2Text
import vlc
from datetime import datetime
import time

class ChatGPT:
	def __init__(self, key = 'Place ChatGPT api key here', messages = [ {"role": "system", "content":
				"You are a intelligent assistant."} ]): #gives role to chatgpt
		self.messages = messages  #messages is a dict
		self.chatgpt_speaker = GText2Speech.Text2Speech() #allows to talk back
		openai.api_key = key

#---FUNCTIONS THAT CONTROL CHAT---------------------------------------------------------

	def start_chat(self):
		microphone = GSpeech2Text.Speech2Text()
		while True:
			#message captured from microphone
			message = str(microphone.capture_noisy())
			print(message)
			if message.lower() == 'quit': #makes sure this an easy way to quit
				self.quit_chat() #quit
				break
			elif message.lower() == 'exit': #quits without saving
				self.exit_chat() #quit no save
			if message:
				self.messages.append(
					{"role": "user", "content": message},
				)
				chat = openai.ChatCompletion.create(
					model="gpt-3.5-turbo", messages=self.messages
				)
			reply = chat.choices[0].message.content
			
			print(f"ChatGPT: {reply}")
			self.speak_chat(reply) #speaks response
			self.messages.append({"role": "assistant", "content": reply})

	def quit_chat(self):#Simple way of quitting chatGPT with saving
		self.write()
		print('\nQuitting ChatGPT')
		player = vlc.MediaPlayer('Place the directory path to a sound file here')
		player.play() #plays file
		quit()

	def exit_chat(self):#Simple way of quitting chatGPT without saving
		print('\nQuitting ChatGPT')
		quit()


#---FUNCTIONS THAT GIVE FUNCTIONALITY---------------------------------------------------

	def write(self): #keeps a record of all chats for later review
		now = datetime.now() #gets date and time
		
		textfile = open('Place the directory path to a text file here', 'a')
		textfile.write('\n------------------------\n')
		textfile.write(str(now) + '\n')

		for i, item in enumerate(self.messages): #writes to file line by line
			if i == 0: #skips very first line defining the role of chatGPT
				continue
			textfile.write(f'{i}.)  {item["role"]}: {item["content"]} \n')

	def speak_chat(self, reply): #allows chatgpt to speak
		self.chatgpt_speaker.say(reply)

		#stops program until chatgpt finishes speaking
		wait_time = self.chatgpt_speaker.speech_duration()
		time.sleep(wait_time)
		
		player = vlc.MediaPlayer('Place the directory path to output_speech.ogg here')
		player.play() #plays file
		
