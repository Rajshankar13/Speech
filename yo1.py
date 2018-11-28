import speech_recognition as sr
import playsound
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    playsound.playsound('audio.mp3', True)
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    r.energy_threshold = 15000
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
	    playsound.playsound('hello.mp3', True) 
        #speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        #speak("Hold on Suman, I will show you where " + location + " is.")
        os.system("chrome https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hi Suman, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)