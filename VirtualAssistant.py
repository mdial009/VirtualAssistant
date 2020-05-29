# Description: This is a Virtual Assistant program that gets the date, current time,
# Respond back with a random greeting, and return information on a person.
#
#
#
#
# Import the Libraries
import calendar
import os
import random
import warnings
import pyaudio
import speech_recognition as sr
import wikipedia
from gtts import gTTS
import datetime

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
    # Created a empty string calling it data for Google Text-to-Speech to put the recorded audio into.
    data = " "
    # Using a try block to take that audio that was recorded and have Google Text-to-Speech output it as a string(data)
    try:
        data = r.recognize_google(audio)
        print("You Said: " + data)
    except sr.UnknownValueError:  # Checks for a unknown errors
        print("Google Speech Recognition Could Not Understand You")
    except sr.RequestError as e:
        print("Request Results From Google Speech Recognition Service Error" + e)

    return data


# A Function To Get The virtual Assistant Response
def assistantResponse(text):
    print(text)

    # Convert the text to speech
    myobj = gTTS(text=text, lang="en", slow=False, lang_check=True)
    # Save The Converted Audio To A File
    myobj.save("assistant_response.mp3")
    # Play The Converted File
    os.system("start assistant_response.mp3")


# A Function For Wake Word(s) or Phrase
def wakeWord(text):
    WAKE_WORDS = ["Hey Madany", "Hey Madani", "hey madani"]  # A list of Wake Words

    text = (
        text.lower() or text.capitalize()
    )  # Converting The Text To All Lower Case Words

    # Check To See If The Users Command/Text Contains A Wake Word/Phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    # If The Wake Word isn't Found In The Text From The Loop And So It Returns False
    return False


# A Function To Get The Current Date
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # Example Friday
    monthNum = now.month
    dayNum = now.day

    # A List Of Months
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    # A List Of Ordinal Numbers
    ordinalNumbers = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]
    return (
        "Today is "
        + weekday
        + " "
        + month_names[monthNum - 1]
        + " The "
        + ordinalNumbers[dayNum - 1]
        + "."
    )


# A Function To Return A Ranndom Greeting Response
def greeting(text):

    # Greeting Inputs
    Greeting_Inputs = ["Hello", "Hey", "Hola", "Greetings", "Wassup", "Hi"]

    # Greeting Responses
    Greeting_Responses = ["Whats Good", "Hello", "Hey There", "Howdy"]

    # If The Users Input Is a Greeting, Then Return a Randomly Chosen Greeting Response
    for word in text.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Responses) + "."
    # If No Greeting Was Detected Then Return An Empty String
    return ""


# A Function To Get A Persons First And Last Name From the Text
def getPerson(text):

    wordList = text.split()  # Splitting The Text Into A List Of Words

    for i in range(0, len(wordList)):
        if (
            i + 3 <= len(wordList) - 1
            and wordList[i].lower() == "who"
            and wordList[i + 1].lower() == "is"
        ):
            return wordList[i + 2] + " " + wordList[i + 3]


while True:
    # Record The Audio
    text = recordAudio()
    response = " "

    # Check For The Wake Word/Phrase
    if wakeWord(text) == True:
        # print("You Said The Wake Word/Phrase")

        # Check For Greetings By The User
        response = response + greeting(text)

        # Check To See If The User Said Anything Having To Do With The Date
        if "date" in text:
            get_date = getDate()
            response = response + " " + get_date

        # Check To See If The User Said "Who Is"
        if "who is" in text:
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + " " + wiki

        # Check To See If The User Said Anything Having To Do With The Time
        if "time" in text:
            now = datetime.datetime.now()
            meridiem = ""
            if now.hour >= 12:
                meridiem = "P.M"  # Post Meridiem (PM) After Midday
                hour = now.hour - 12
            else:
                meridiem = "A.M"  # Ante Meridiem (AM) Before Midday
                hour = now.hour

            if now.minute < 10:
                minute = "0" + str(now.minute)
            else:
                minute = str(now.minute)
            response = (
                response
                + " "
                + "It Is"
                + str(hour)
                + ":"
                + minute
                + " "
                + meridiem
                + "."
            )
        # Have The Assistant Respond Back Using Audio And The Text From Response
        assistantResponse(response)

# text = "Hey I LOVE YOU SO MUCH IS THIS NOT AWESOME RIGHT??"
# assistantResponse(text)
# recordAudio()
# print(getDate())
