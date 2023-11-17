import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui 
import pywhatkit as pkit
import time


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
            voice_input=r.recognize_google(message,language='en-in')   #Recognizing the input of user using Google Web Speech API
            print(f'User said: {input}\n')
            return voice_input
    except Exception as e:
        print('Unable to recognize,please say that again..')
        return 'None'
    
   

def greet():
    engine.say('ByteVoice Activated!!!')
    engine.say('Hello,I am ByteVoice. I am here to help you!!! Can you specify, what should I do for you ?')
    engine.runAndWait()
    
def speak(message):
    engine.say(message)
    engine.runAndWait()
    
    
if __name__=="__main__":
    greet()
    while True:
        user_input=userCommand()          #Getting the commands of user in the form of list
        
        if user_input != 'None':
            input_text = user_input.lower()            # type: ignore
        else:
            print('Recognition failed,Please try again')
            continue
        
        if 'wikipedia' in input_text:                            #Checking if user asks for wikipedia command
            speak('Searching Wikipedia')
            input_text=input_text.replace('wikipedia','')       #Extracting only the topic to be searched from the user input voice data
            info=wikipedia.summary(input_text,sentences=2)       #Searching info about topic
            speak(info)
            
        elif 'open google' in input_text:
            webbrowser.open('google.com')                        #Opening google.com
            
        elif 'close google' in input_text:
            pyautogui.hotkey('ctrl','w')                         #Shortcut for closing any window => ctrl+w
        
        elif 'open youtube' in input_text:                       #Opening youtube
            webbrowser.open('youtube.com')
        elif 'close youtube'in input_text:
             pyautogui.hotkey('ctrl','w') 
        elif 'search google' in input_text:
            speak('What should I search for???')
            speak('Opening Google')
            search_input=userCommand()                            #Reciving user's input for topic of search
            webbrowser.open(f'https://www.google.com/search?q={search_input}')     #Embeding the topic in url,using google's search format 
        elif 'search youtube' in input_text:
            speak('What should I search for???')
            search_input=userCommand()
            speak('Opening YouTube')
            webbrowser.open('youtube.com')
            time.sleep(2)                                            #Waiting for youtube to open
            pyautogui.press('/')                                     #Shortcut for selecting youtube search box
            pyautogui.typewrite(f'{search_input}')                  # Typing the voice input in the YouTube search bar
            pyautogui.press('enter')                                # Press Enter to start the search
        elif 'take screenshot' in input_text:
            speak('Taking screenshot')
            img=pyautogui.screenshot('Byte-Voice/myscreenshot.png')
            speak('Screenshot saved successfully!!')
            break
            
            
            
        
            
            
            
        