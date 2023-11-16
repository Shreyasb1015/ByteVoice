import pyttsx3
import speech_recognition as sr

#Intiliazing the TTS engine and loading the driver object of device.
engine=pyttsx3.init('sapi5')

#Getting the voice property of the engine.
voices=engine.getProperty('voice')

engine.setProperty('voice',voices[0])     #voices[0] represent male voice
engine.setProperty('rate', 150)  
engine.setProperty('volume', 0.7)  

#This function is implemented to take the user's input.
def userCommand():  
    
    r=sr.Recognizer()   #Creating the instance of Recognizer class
    with sr.Microphone() as source:   #opennig a connection to the computer's microphone
        print('Listening.....')
        r.pause_threshold=1       #Setting the threshold(amount of silence to needed to determine end of user's input) to 1
        message=r.listen(source)   #Capturing the user's input with the microphone in the message variable
        
    try:
            print('Recognizing...')
            input=r.recognize_google(message,language='en-in')   #Recognizing the input of user using Google Web Speech API
            print(f'User said: {input}\n')
    except Exception as e:
        print('Unable to recognize,please say that again..')
        return 'None'
    return input

def greet():
    engine.say(' ByteVoice Activated...........Hello!!! I am ByteVoice. I am here to help you!!! Can you specify, what should I do for you ?')
    engine.runAndWait()
if __name__=="__main__":
    greet()
        