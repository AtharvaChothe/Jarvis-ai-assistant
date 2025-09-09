import requests
import model
from model import speak 
from model import listen_for_input
import pywhatkit
import datetime
import pyautogui
import time
import eel

import google.generativeai as genai
import speech_recognition as sr

# Configure the Gemini API key
genai.configure(api_key='AIzaSyBKamzUV21kt1Ce6rd_f42Ixlsy9hitJRU')

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_content(input_text):
    try:
        # Start a new chat session
        chat = model.start_chat()

        # Send the user's message and get the response
        response = chat.send_message(input_text)

        # Print and return the generated response
        print("Gemini Response:", response.text)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return str(e)








# Make sure you have your voice functions imported
# from your previous code: listen_for_input() and speak()
# Listen to the user's question
user_input = listen_for_input()

# Generate Gemini response **only once**
first_response = generate_content(user_input)


print("Gemini Response:", first_response)
#speak(first_response)  # Speak the response if you want

# Ask if user wants to send via WhatsApp
print("Do you want to send this text to WhatsApp?")
speak("Do you want to send this text to WhatsApp?")
confirmation = listen_for_input()

confirmation = confirmation.lower()
if "yes" in confirmation or "send it" in confirmation:
    number = "+917387595211"  # Or get dynamically via voice
    speak("Sending your message now.")
    try:
        # Send only the **first response**
        pywhatkit.sendwhatmsg_instantly(number, first_response, wait_time=10, tab_close=False)
        time.sleep(5)
        pyautogui.press("enter")
        speak("Message sent successfully.")
           
    except Exception as e:
        print(f"Error sending message: {e}")
        speak("Sorry, I couldn't send the message.")
else:
    speak("Okay, not sending the message.")
1


# Initialize and start the app


if __name__ == "__main__":
    question = listen_for_input()
   
