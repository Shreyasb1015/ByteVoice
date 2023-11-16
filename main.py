import pyttsx3

#Intiliazing the TTS engine and loading the driver object of device.
engine=pyttsx3.init('sapi5')

#Getting the voice property of the engine.
voices=engine.getProperty('voice')

engine.setProperty('voice',voices[0]) #voices[0] represent male voice
engine.setProperty('rate', 150)  #  Setting the speed of speech
engine.setProperty('volume', 0.7)  # Setting the volume level

engine.say('Hello Guys!! I am byte-voice.')
engine.runAndWait()   #Waiting for the sentence to be finished.