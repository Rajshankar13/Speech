import speech_recognition as sr

r=sr.Recognizer()
r.energy_threshold = 15000

with sr.Microphone() as source:
	print("This is Speech2Text Demo")
	audio = r.listen(source)

try:
	print("Using Google API:\n" + r.recognize_google(audio))

except:
	pass