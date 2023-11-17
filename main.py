import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui 
import pywhatkit as pkit
import time
import os
import random

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

def photo():
    speak('Opening Camera')
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.typewrite('camera')
    time.sleep(3)
    pyautogui.press('enter')
    speak('Say Chesse!!')
    time.sleep(2)
    pyautogui.press('enter')
    speak('Photo Saved successfully!!')
    
def open_intellij():
    speak('Opening intellij')
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.typewrite('intellij')
    time.sleep(2)
    pyautogui.press('enter')
    

def close_wind():
     pyautogui.hotkey('alt','f4') 
     

def open_vscode():
    speak('Opening vscode')
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.typewrite('vscode')
    time.sleep(2)
    pyautogui.press('enter')
    

    
if __name__=="__main__":
    greet()
    while True:
        user_input=userCommand()                                  #Getting the commands of user in the form of list
        
        if user_input != 'None':
            input_text = user_input.lower()                       # type: ignore
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
            search_input=userCommand()                                          #Reciving user's input for topic of search
            speak('Opening Google')                       
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
            speak('Specify the name for yout file.')
            name=userCommand().lower()              #type:ignore
            time.sleep(3)                                             #Waiting for user to send input
            speak('Taking screenshot')
            img=pyautogui.screenshot(f'Byte-Voice/{name}.png')        #Saving the screenshot as per user's filename
            speak('Screenshot saved successfully!!')
            
        elif 'play music' in input_text:
            music_dir='C:\\Users\\bagwe\\Music'                         #specifying path of music directory
            songs=os.listdir(music_dir)                                 #Getting the list of all songs in directory
            play_song= random.choice(songs)                             #Choosing random song from the list of songs
            os.startfile(os.path.join(music_dir,play_song))             #Starting the file using os.startfile()
            
        elif 'stop music' in input_text:
            os.system('taskkill /f /im "Microsoft.Media.Player.exe"')    #Specifying process name to terminate the process.
        
        elif 'click photo' in input_text:
            photo()                                                        #Calling photo function
        
        elif 'stop camera' in input_text:
            speak('closing camera')
            pyautogui.hotkey('alt','f4')                                   #Closing the current window
        
        elif 'open command prompt'in input_text:
            speak('Opening command prompt')
            #Opening command prompt
            os.system('start cmd')    
          
        elif 'close command prompt' in input_text:
            speak('Closing command prompt')
            #Terminating the process and closing command prompt
            os.system('taskkill /f /im "WindowsTerminal.exe"')             
            
        elif 'open java code editor' in input_text or 'open kotlin code editor' in input_text:
            open_intellij()
            
        elif 'close window' in input_text:
            close_wind()
            break
        elif 'open vscode' in input_text:
            open_vscode()
            break