# RUXpyN-Pi4
The working version of RUXpyN for Raspberry Pi 4

created by Alicia Ramos and Bryan Toscano 'hyde'

This version will work on the Raspberry Pi Desktop released on July 1st, 2022.

----------------------------------------------------------------------------------------------
These are the packages you need to install and the commands to install them:

pip install openai
pip install pyaudio
pip install SpeechRecognition pydub
pip install gTTS
pip install mutagen
pip install python-vlc
apt-get install portaudio19-dev python3-pyaudio
apt-get install flac

----------------------------------------------------------------------------------------------
The initial setup needs directories to be changed and you need an OpenAi ChatGPT API key.


How to use RUXpyN:
1. Open the terminal and navigate to the directory holding all the files.
2. To run once type "python3 main.py" or to run infinitely type "./loop.exe"
3. RUXpyN will be looking for a Wake Word.  The default Wake Word is "Hey PYN" which can be changed to whatever the user desires.
4. After the RUXpyN wakes, the user will hear a sound.  Informing the user that RUXpyN is ready for input. This is where the user can ask it any question they desire.
5. After RUXpyN has spoken and you hear another sound indicating RUXpyN is ready for more input.
6. If the user ever wants to end talking with RUXpyN, they can say quit.  This will write the conversation to a text file called chat_log.txt and this will cause RUXpyN to close and reopen. Now RUXpyN will be waiting for the Wake Word again if the user has chosen the infinite version. If the user chose the single run, it will now close RUXpyN fully.

----------------------------------------------------------------------------------------------
Issues Encountered

-Running out of Memory.  After running RUXpyN for about 10 minutes, we started having memory issues.  We got "memory cannot be allocated" errors, so in order to mitigate that, it is important to say quit so that the program can close.  If using the infinite version, this will cause the program to close, free up memory, and start up fresh.

-Server Errors.  Sometimes we would get issues relating to name resolution or server busy.  This is due to us having low priority with our API calls.  Since we are using free versions of everything, we have low priority with our calls.  These can also be caused by connection issues or servers being down.

-Unknown Value Error.  This would happen when RUXpyN was unsure of what the user said.  The solution was to create an exception and ask for the input again.
