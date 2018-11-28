import tkinter as tk
from functools import partial
import speech_recognition as sr
import playsound
from time import ctime
import time
import os
from gtts import gTTS
def speak(result1,result2,result3):
    result1.config(text="Please speak operation!")
    r = sr.Recognizer()
    r.energy_threshold = 15000
    with sr.Microphone() as source:
        audio = r.listen(source)
    opt=" "
    try:
        opt = r.recognize_google(audio)
        result2.config(text="You said :"+opt)
        result3.config(text="Please speak numbers!")
    except sr.UnknownValueError:
        print("Could not understand audio")       
    except sr.RequestError as e:
        print("could not request results;{0}".format(e))
    data1 = recordAudio(result2)
    data2 = recordAudio(result2)
    if(opt == "addition"):
        s = int(data1) + int(data2) 
        result3.config(text="Sum of numbers is %d " % s)           
    elif(opt == "subtraction"):
        d = int(data1) - int(data2)
        result3.config(text="Difference of numbers is %d " % d)
    elif(opt == "multiplication"):
        m = int(data1) * int(data2)
        result3.config(text="Product of numbers is %d" % m)
    else:
        divide = int(data1) / int(data2)
        result3.config(text="Division of numbers is %d" % divide)

def recordAudio(result2):
    r = sr.Recognizer()
    r.energy_threshold = 15000
    with sr.Microphone() as source: 
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        result2.config(text="You said : " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return data
    
def add(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)+float(b)
	result3.config(text="Sum of numbers is %d" % c)
def sub(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)-float(b)
	result3.config(text="Subtraction of numbers is %d" % c)
def mul(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)*float(b)
	result3.config(text="Product of numbers is %d" % c)
def div(result3,n1,n2):
	a=(n1.get())
	b=(n2.get())
	c=float(a)/float(b)
	result3.config(text="Division of numbers is %d" % c)
def clear():
    num1.delete(0,30)
    num2.delete(0,30)
    result1.config(text=" ")
    result2.config(text=" ")
    result3.config(text=" ")
root=tk.Tk()
root.geometry('500x300+100+200')
root.title("Calculator")
label=tk.Label(root,text="Number 1 :",fg="blue")
label.grid(row=1,column=0)
label1=tk.Label(root,text="Number 2 :",fg="blue")
label1.grid(row=2,column=0)
number1=tk.StringVar()
number2=tk.StringVar()
num1=tk.Entry(root,textvariable=number1)
num1.grid(row=1,column=1)
num2=tk.Entry(root,textvariable=number2)
num2.grid(row=2,column=1)
result1=tk.Label(root,fg="blue")
result1.grid(row=9,column=0)
result2=tk.Label(root,fg="blue")
result2.grid(row=10,column=0)
result3=tk.Label(root,fg="green")
result3.grid(row=11,column=1)
add=partial(add,result3,number1,number2)
addition=tk.Button(root,text="Add",width=6,bg="blue",command=add)
addition.grid(row=5,column=0)
sub=partial(sub,result3,number1,number2)
subtraction=tk.Button(root,text="Subtract",width=8,bg="blue",command=sub)
subtraction.grid(row=5,column=1)
mul=partial(mul,result3,number1,number2)
multiplication=tk.Button(root,text="Multiply",width=8,bg="blue",command=mul)
multiplication.grid(row=6,column=0,padx=5)
div=partial(div,result3,number1,number2)
division=tk.Button(root,text="Divide",width=7,bg="blue",command=div)
division.grid(row=6,column=1,padx=3)
clr=tk.Button(root,text="Clear",bg="yellow",command=clear)
clr.grid(row=6,column=2)
speak=partial(speak,result1,result2,result3)
say=tk.Button(root,text="Speak",bg="red",width=6,command=speak)
say.grid(row=7,column=1)
root.mainloop()