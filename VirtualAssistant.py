# Description: This is a Virtual Assistant program that gets the date, current time,
# Respond back with a random greeeting, and return information on a person.
#
#
#
#
#
#
#
#
#
# Ingores any warning messages
import pyaudio 
import speech_recognition as sr
import os
import datetimepi
import warnings
import calendar
import random
import wikipedia
from gtts import gTTS
import sys
print(sys.version)
print(sys.executable)

# Ingores any warning messages
warnings.filterwarnings("ignore")

# A fuction thats going to records audio and return it as a string


def recordAudio():

    # Record the audio
    r = sr.Recognizer()  # Creating a recognizer object

    # Open the microphone and start recording
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)

    # Use Google Speech Recognition
    data = " "
    try:
        data = r.recognize_google(audio)
        print("You Said: "+data)
    except sr.UnknownValueError:  # Checks for a error
        print("Google Speech Recognition Could Not Understand You")
    except sr.RequestError as e:
        print("Request Results from Google Speech Recognition Service Error" + e)

    return data


recordAudio()
