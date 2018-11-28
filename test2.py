from tkinter import Tk,Button,Label
import speech_recognition as sr
import playsound
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("audio1.mp3")
	playsound.playsound('audio1.mp3', True)

def recordAudio():
	r = sr.Recognizer()
	r.energy_threshold = 15000
	with sr.Microphone() as source:
		print("Speak Number 1!")
		audio = r.listen(source)
	global data
	try:
		data = r.recognize_google(audio)
		print("You said: " + data)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return data
def recordAudio1():
	r = sr.Recognizer()
	r.energy_threshold = 15000
	with sr.Microphone() as source:
		print("Speak Number 2!")
		audio = r.listen(source)
	global data1
	try:
		data1 = r.recognize_google(audio)
		print("You said: " + data1)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return data1


speak("Hello, what operation you want to perform?")
r = sr.Recognizer()
r.energy_threshold = 15000
with sr.Microphone() as source:
	audio = r.listen(source)
opt=""
try:
	opt = r.recognize_google(audio)
	print("You said: " + opt)
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
root = Tk()
time.sleep(2)

b1 = Button(root, fg = 'pink', bg = 'purple', text = 'Enter Number 1', command = recordAudio)
b1.pack()
b2 = Button(root, fg = 'pink', bg = 'purple', text = 'Enter Number 2', command = recordAudio1)
b2.pack()
root.mainloop()
#data1 = recordAudio()
#data2 = recordAudio()
if(opt == "addition"):
	s = int(data) + int(data1)
	print(s)
elif(opt == "subtraction"):
	d = int(data) - int(data1)
	print(d)
elif(opt == "multiplication"):
	m = int(data) * int(data1)
	print(m)
elif(opt == "division"):
	div = float(data) / float(data1)
	print(div)
elif(opt == "conversion"):
	print("This converts kmph to m/s")
	conv = float(5/18) * float(data)
	print(conv)
else:
	print("Sorry, I am not programmed to perform this operation")

