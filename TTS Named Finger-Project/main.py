#*******TTS Named Finger : Text to Speech converter - by ExE -***********

#import libraries (tkinter , gTTS  , playsound & os)
import tkinter
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
"""  
for the GUI
"""
from gtts import gTTS
"""
for convert text in speech
"""
from playsound import playsound
"""
for reproduce gTTS file
"""
from os import remove


#TTS 

def Text_to_speech():
    mssg = entry_field.get()
    speech = gTTS(text = mssg, lang='en', slow=False)
    speech.save("text.mp3")
    playsound("text.mp3")
    remove("text.mp3")

def exit():
    window.destroy()

def delete():
    Message.set("")


#GUI

window = tkinter.Tk()
image0 = Image.open('img/WalterputyouDaway.png')
bckend = ImageTk.PhotoImage(image0)
window.geometry("1400x700")
lbl = tkinter.Label(window, image=bckend)
lbl.place(x=0, y=0)
window.title('TTS Named Finger : Text to Speech Converter')
window.iconbitmap('img/mainIcon.ico')


title = tkinter.Label(window, text="TTS Named Finger - by ExE -",font =('Times New Roman bold', 20))
title.pack(fill = tkinter.X)
text = tkinter.Label(window, text="Insert the f*ckin text here : ",font=('Times New Roman underline', 25) )
text.place(x=140, y=210)
Message = tkinter.StringVar()
entry_field= tkinter.Entry(window,textvariable=Message, width=65 )
entry_field.place(x=170, y=305, height=50)

button = ttk.Button(text="Exit", command=exit)
button.place(x=200, y=400)
button = ttk.Button(text="Convert!", command=Text_to_speech)
button.place(x=300, y=400)
button = ttk.Button(text="Clear", command=delete)
button.place(x=400, y=400)


window.mainloop()

