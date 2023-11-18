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
    
    #Creating the instance of Recognizer class
    r=sr.Recognizer()   
    #opening a connection to the computer's microphone
    with sr.Microphone() as source:  
        print('Listening.....')
        r.pause_threshold=1       #Setting the threshold(amount of silence to needed to determine end of user's input) to 1
        message=r.listen(source)   #Capturing the user's input with the microphone in the message variable
        
    try:
            print('Recognizing...')
            voice_input=r.recognize_google(message,language='en-in')   #Recognizing the input of user using Google Web Speech API
            print(f'User said: {voice_input}\n')
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
    #Searching for camera in windows search bar
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


#This is dictionary for storing code snippets of various languages. 
code_snippets = {
    'C language': '''
#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}
''',
    'python': '''
print("Hello, World!")
''',
    'c++': '''
#include <iostream>

int main() {
    // Write C++ code here
    std::cout << "Hello world!";
    return 0;
}
''',
    'JavaScript': '''
console.log("Welcome to Programiz!");
''',
    'Java': '''
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
''',
    'HTML': '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a sample HTML page.</p>
</body>
</html>
''',
    'CSS': '''
body {
    font-family: 'Arial', sans-serif;
    background-color: #f0f0f0;
    color: #333;
    margin: 20px;
}

h1 {
    color: #0066cc;
}

p {
    line-height: 1.6;
}
'''
}

def newFile():
    
    speak('please specify filename')
    file_name=userCommand()

    speak('Please specify your programming language')
    language=userCommand()
    extension=''
    
    if language =='python':
        extension='py'
    elif language =='C language':
        extension='c'
    elif language == 'c++':
        extension= 'cpp'
    elif language== 'Java':
        extension='java'
    elif language == 'javaScript':
        extension='js'
    elif language == 'HTML':
        extension = 'html'
    elif language == 'CSS':
        extension ='css'
    
    #Creating command format
    command = f'code {file_name}.{extension}'      
     
    #Running the command in terminal
    os.system(command)                            
    
  
    if language in code_snippets:
        code_snippet = code_snippets[language]       #type:ignore
        pyautogui.typewrite(code_snippet)
    
    speak('file created successfully!!!')
        
                
if __name__=="__main__":
    greet()
    while True:
        user_input=userCommand()                                  #Getting the commands of user in the form of list
        
        if user_input != 'None':
            input_text = user_input.lower()                       # type: ignore
        else:
            print('Recognition failed,Please try again')
            continue
        
        #Checking if user asks for wikipedia command
        if 'wikipedia' in input_text:                           
            speak('Searching Wikipedia')
            input_text=input_text.replace('wikipedia','')       #Extracting only the topic to be searched from the user input voice data
            info=wikipedia.summary(input_text,sentences=2)       #Searching info about topic
            speak(info)
            
        elif 'open google' in input_text:
            #Opening google.com
            webbrowser.open('google.com')   
                               
        elif 'close google' in input_text:
            pyautogui.hotkey('ctrl','w')                         #Shortcut for closing any window => ctrl+w
        
        elif 'open youtube' in input_text:     
            #Opening youtube                 
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
            #Waiting for youtube to open
            time.sleep(2)                                           
            pyautogui.press('/')                                     #Shortcut for selecting youtube search box
            # Typing the voice input in the YouTube search bar
            pyautogui.typewrite(f'{search_input}')  
            # Pressing Enter to start the search               
            pyautogui.press('enter')         
                                   
        elif 'take screenshot' in input_text:
            
            speak('Specify the name for yout file.')
            name=userCommand().lower()              #type:ignore
            #Waiting for user to send input
            time.sleep(3)                                            
            speak('Taking screenshot')
            #Saving the screenshot as per user's filename
            img=pyautogui.screenshot(f'Byte-Voice/{name}.png')        
            speak('Screenshot saved successfully!!')
            
        elif 'play music' in input_text:
            
            #specifying path of music directory
            music_dir='C:\\Users\\bagwe\\Music'    
            #Getting the list of all songs in directory                    
            songs=os.listdir(music_dir)    
            #Choosing random song from the list of songs                           
            play_song= random.choice(songs)  
            #Starting the file using os.startfile()                           
            os.startfile(os.path.join(music_dir,play_song))          
            
        elif 'stop music' in input_text:
            #Specifying process name to terminate the process.
            os.system('taskkill /f /im "Microsoft.Media.Player.exe"')  
            
        elif 'volume up' in input_text:
            pyautogui.press('volumeup')
        
        elif 'volume down' in input_text:
            pyautogui.press('volumedown')
        
        elif 'volume mute' in input_text:
            pyautogui.press('volumemute')  
        
        elif 'click photo' in input_text:
             #Calling photo function
            photo()                                                      
        
        elif 'stop camera' in input_text:
            speak('closing camera')
            #Closing the current window
            pyautogui.hotkey('alt','f4')   
                                            
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
            
        elif 'open vscode' in input_text:
            open_vscode()
            
        elif 'create code file' in input_text:
            newFile()
            break