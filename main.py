import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui 
import pywhatkit as pkit
import time
import os
import random
import asyncio
from jokeapi import Jokes 
import requests
import tkinter as tk
from tkinter import messagebox
import wolframalpha
import base64
from urllib.request import urlopen


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
    
def search_wiki(input_text):
    
     input_text=input_text.replace('wikipedia','')            #Extracting only the topic to be searched from the user input voice data 
     speak('Searching Wikipedia')    
     info=wikipedia.summary(input_text,sentences=2)       #Searching info about topic
     speak(info)

def write_note():
    speak('Opening Notepad')
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.typewrite('notepad')
    time.sleep(3)
    pyautogui.press('enter')
    speak('Please specify your notes')
    notes=userCommand().lower()                                  #type:ignore
    pyautogui.typewrite(notes)
    time.sleep(5)
    speak('Notes added successfully!!!')
    

async def tell_joke():
     j = await Jokes()  # Initialise the class
     joke = await j.get_joke(response_format="txt")  # Retrieving a random joke
     print(joke)
     speak(joke)           
    

def get_weatherinfo(city):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': '897d6cb747ac9abbdc978c14364c1925',
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extracting relevant weather information
            main_weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Formatting the weather information
            weather_info = f"Weather in {city}: {main_weather}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s."
            return weather_info
        else:
            return f"Error: {data['message']}"

    except requests.RequestException as e:
        return f"Error: {e}"  


def fetch_random_riddle():
    api_url = "https://riddles-api.vercel.app/random"
    response = requests.get(api_url)
    print(response)

    if response.status_code == 200:
        riddle_data = response.json()
        return riddle_data.get("riddle", ""), riddle_data.get("answer", "")
    else:
        return None, None


def guess_riddle():
    
      riddle_question, correct_answer = fetch_random_riddle()
      if riddle_question and correct_answer:
        speak("Here's a riddle for you:")
        time.sleep(1)
        print(riddle_question)
        #Asking riddle question to the user
        speak(riddle_question)
       
        
        #Getting the guess of user
        user_guess=userCommand()
        if user_guess.lower() == correct_answer.lower():         #type:ignore
            speak("Congratulations!!! Your guess is correct.You seems to be a talented person")
        else:
            #Printing the correct answer
            print(f'Correct answer is {correct_answer}')
            speak(f"Oops!!!Sorry, the correct answer is {correct_answer}.")
           
      else:
          #Handling the data fetching errors.
        speak("Sorry, there was an error fetching the riddle. Please try again later.")
    


class MeditationTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meditation Timer")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Enter meditation time (in seconds):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack()

    def start_timer(self):
        try:
            meditation_time = int(self.entry.get())
            if meditation_time <= 0:
                messagebox.showerror("Error", "Please enter a valid meditation time.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        self.root.withdraw()  # Hiding the main window during the meditation

        # Creating a new window for the countdown
        countdown_window = tk.Toplevel()
        countdown_window.title("Meditation Timer")
        countdown_window.geometry("300x200")

        countdown_label = tk.Label(countdown_window, text=f"Time remaining: {meditation_time} seconds")
        countdown_label.pack(pady=10)

        start_time = time.time()
        end_time = start_time + meditation_time

        while time.time() < end_time:
            remaining_time = int(end_time - time.time())
            time_str = f"Time remaining: {remaining_time} seconds"
            countdown_label.config(text=time_str)
            countdown_window.update()
            time.sleep(1)

        time.sleep(2)
        print('Meditation Time over')
        speak('Over!!!')
        # Showing a message when the meditation is complete
        messagebox.showinfo("Meditation Timer", "Meditation complete!")

        # Closing the countdown window
        countdown_window.destroy()

        # Showing the main window again
        self.root.deiconify()

def tell_quote():
    api_url = "https://type.fit/api/quotes"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if data:
            random_quote = random.choice(data)
            quote_text = random_quote.get("text", "No quote text available")
            quote_author = random_quote.get("author", "Unknown author")
            
            speak(f'"{quote_text}"')
        else:
            speak("Unable to fetch quotes at the moment.")
    
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while fetching quotes.")


def ans_to_que(query, app_id):
    
    # Initializing the Wolfram Alpha client
    client = wolframalpha.Client(app_id)

    try:
        # Performing the query to Wolfram Alpha
        res = client.query(query)

        # Parsing the result
        answer = next(res.results).text

        #returning the answer
        return answer

    except StopIteration:
        
        return "Sorry, I couldn't find a relevant answer."
    
def math(canvas,entry1):
    
 
    API_KEY = 'KH7XAP-8P76865RYR'
    client = wolframalpha.Client(API_KEY)

    eq = entry1.get()            #To get the input entered by user.
    res = client.query(eq.strip(), params=(("format", "image,plaintext"),))
    #Creating empty dictionary
    data = {}  

    for p in res.pods:
        for s in p.subpods:
            if s.img.alt.lower() == "root plot":
                #Extracting root plot
                data['rootPlot'] = s.img.src            
            elif s.img.alt.lower() == "number line":
                #Extracting number line
                data['numberLine'] = s.img.src

    data['results'] = [i.texts for i in list(res.results)][0]

    #Printing data 
    print(data)

    if 'rootPlot' in data:
        image1_url = data['rootPlot']
        image1_byt = urlopen(image1_url).read()
        image1_b64 = base64.encodebytes(image1_byt)
        photo1 = tk.PhotoImage(data=image1_b64)
        canvas.photo1 = photo1
        canvas.create_image(10, 30, image=canvas.photo1, anchor='nw')
        canvas.create_text(175, 40, fill="darkblue", font="Arial 10", text="Root Plot")

    if 'numberLine' in data:
        image2_url = data['numberLine']
        image2_byt = urlopen(image2_url).read()
        image2_b64 = base64.encodebytes(image2_byt)
        photo2 = tk.PhotoImage(data=image2_b64)
        canvas.photo2 = photo2
        canvas.create_image(10, 240, image=canvas.photo2, anchor='nw')
        canvas.create_text(175, 230, fill="darkblue", font="Arial 10", text="Number Line")

    # Display the result text
    canvas.create_text(175, 320, fill="darkblue", font="Arial 15", text=data.get('results', 'No Results'))
    
list_command=['wikipedia','open google','close google','open youtube','close youtube','search google','search youtube','take screenshot','play music','stop music',
              'volume up','volume down','volume mute','click photo','stop camera','open command prompt','close command prompt','open java code editor',
              'open kotlin code editor','close window','open vscode','create code file','refresh the screen','scroll down','scroll up','thanks bytevoice',
              'write in notepad','close notepad','developer information','tell me a joke','weather update','ask me a riddle','tell me a quote','set meditation timer',
              'answer my question','solve maths question','exit'
    
    ]
   
    
def main():
    greet()
    display_math_window = False  
    while True:
        user_input=userCommand()                                  #Getting the commands of user in the form of list
        
        if user_input != 'None':
            input_text = user_input.lower()                       # type: ignore
        else:
            print('Recognition failed,Please try again')
            continue
        
        #Checking if user asks for wikipedia command
        if 'wikipedia' in input_text:                           
           
            search_wiki(input_text)
            
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
            #Calling open_intellij function
            open_intellij()
            
        elif 'close window' in input_text:
            #Calling close_wind function
            close_wind()
            
        elif 'open vscode' in input_text:
            #Calling open_vscode function
            open_vscode()
            
        elif 'create code file' in input_text:
            #Calling newfile function
            newFile()
        
        elif 'refresh the screen' in input_text:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        
        elif 'scroll down' in input_text:
            #Passing positive value to scroll down
            pyautogui.scroll(1000)
        
        elif 'scroll up ' in input_text:
            #Passing negative value to scroll up
            pyautogui.scroll(-1000)
        
        elif 'thanks bytevoice' in input_text:
            speak('Its my pleasure!!!')
        
        elif 'write in notepad' in input_text:
            #Calling write_note function
            write_note()
        
        elif 'close notepad' in input_text:
            
            #terminating ongoing process
            os.system('taskkill /f /im "Notepad.exe"')
        
        elif 'developer information' in input_text:
            
            speak('Name of my developer is Shreyas Bagwe.')
            time.sleep(1)
            speak('Opening his github page')
            webbrowser.open('https://github.com/Shreyasb1015')
        
        elif 'tell me a joke' in input_text:
            asyncio.run(tell_joke())
        
        elif 'weather update' in input_text:
            speak('Please,specify your location')
            #Receiving location from user
            loc=userCommand()
            #Calling get_weather function
            weather_info=get_weatherinfo(loc)
            speak(weather_info)
        
        elif 'ask me a riddle' in input_text:
            
            #Calling the guess_riddle function
            guess_riddle()
            break
        
        elif 'tell me a quote' in input_text:
            tell_quote()   
            
        elif 'set meditation timer' in input_text:
            root = tk.Tk()
            app = MeditationTimerApp(root)
            root.mainloop()
        
        elif 'answer my question'in input_text:
             
            wolfram_app_id = "KH7XAP-8P76865RYR" 
            speak('Please ask me any mathematical or scientific question') 
            user_query = userCommand()
            result = ans_to_que(user_query, wolfram_app_id)
            speak(result)
            print(result)
            
        elif 'solve maths question' in input_text:
            
            speak('Opening maths solver')
            root = tk.Tk()
            root.title("Math Solver")

            #Setting dimensions of root page
            w = 500
            h = 500
            x = 50
            y = 100

            root.geometry("%dx%d+%d+%d" % (w, h, x, y))

            # creating a white canvas
            canvas = tk.Canvas(bg='white')
            canvas.config(height=350)
            canvas.pack()

            # creating entry box to get user input
            entry1 = tk.Entry(root) 
            canvas.create_window(150, 15, window=entry1)

            #  creating submit button
            submit = tk.Button(text='Solve',command=lambda: math(canvas, entry1),height=2, width = 5)  #type:ignore
            canvas.create_window(280, 15, window=submit)

            #calling math function
            root.mainloop()
            # math(canvas,entry1)
        
        elif 'list all commands' in input_text:
            speak('Listing all  supported commands') 
            print(list_command)       
                    
        elif 'exit' in input_text:
            speak('Hope you enjoyed my services!!!Signing off!!')
            break
        
if __name__=='__main__':
    main()