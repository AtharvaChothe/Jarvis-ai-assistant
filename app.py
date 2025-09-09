import sys
from urllib import request
import pyttsx3
import speech_recognition as sr
import webbrowser
import subprocess
import pywhatkit
import datetime
import pyautogui
import time
import eel

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


import sys
from io import StringIO
import eel  # Make sure eel is imported first

# Initialize eel first


class FrontendOutput(StringIO):
    def __init__(self, original_stdout):
        super().__init__()
        self.original_stdout = original_stdout
        self.buffer = ""
    
    def write(self, text):
        self.buffer += text
        if '\n' in self.buffer:  # Send complete lines
            lines = self.buffer.split('\n')
            for line in lines[:-1]:  # Send all complete lines
                line = line.strip()
                if line:
                    eel.DisplayMessage(line + "\n")  # Send to frontend
                    self.original_stdout.write(line + "\n")  # Console
            self.buffer = lines[-1]  # Keep incomplete last line
    

# Store the original stdout
original_stdout = sys.stdout
original_stderr = sys.stderr

# Create and assign our custom output
sys.stdout = FrontendOutput(original_stdout)
sys.stderr = FrontendOutput(original_stderr)






def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        #eel.DisplayMessage('Listening for command...')
        #speak("How can I help you?")

        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)

    try:
        print('recognizing')
        #eel.DisplayMessage('recognizing')
        content = r.recognize_google(audio, language='en-IN')
        print(f"You said: {content}")
       # eel.DisplayMessage(content)
        return content
    except Exception as e:
        print("Sorry, I didn't catch that. Please try again.")
        return ""

@eel.expose

def main_process():
        request = command().lower()
  
       
        if "open instagram" in request:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com/accounts/login/")
        elif "open youtube" in request:                                                  
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        
        elif "open whatsapp" in request:
            speak("Opening WhatsApp")
            subprocess.run([
            "powershell",
            "start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
        
    ])
        

        
        elif "youtube" in request:
            print("tell me video")
            speak("tell me video")
            w=command()
            pywhatkit.playonyt(w)
            time.sleep(4)
            pyautogui.press("enter")


eel.init('frontend')
eel.start('index.html', port=0)
