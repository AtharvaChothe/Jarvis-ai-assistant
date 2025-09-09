import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import time


# Initialize recognizer
recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("Listening for your question...")  # Let the user know it's listening
#speak("Listening for your question...")

def listen_for_input():
    with sr.Microphone() as source:
        
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)  # Listen to the audio
        
        # Convert speech to text using Google's API
        try:
            print("Recognizing...")
            speak("Recognizing..")
            text = recognizer.recognize_google(audio)  # You can also use recognize_bing, recognize_sphinx, etc.
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, I'm unable to process your request at the moment.")
            speak("Sorry, I'm unable to process your request at the moment.")
            return None


