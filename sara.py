import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import playsound
from gtts import gTTS
import os
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def take_command():
    try:
        with sr.Microphone() as mp:
            talk("How can I help you?")
            print('listening...')
            voice = listener.listen(mp)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'sara' in cmd:
                cmd=cmd.replace('sara','')
                
    except:
        pass
    return cmd
def run_sara():
    talk("Hi, I am your personal desktop assistant")
    command=take_command()
    print(command)
    
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        tm=datetime.datetime.now().strftime('%I %M %p')
        print(tm)
        talk('Current time is' +tm)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'sleep' in command:
        talk("Ok bye and take care")
        exit()
        
    elif 'search'  in command:
            sear = command.replace('search','')
            pywhatkit.search(sear)
    
    else:
        talk('Sorry, Please say the command again')


while(True):
    run_sara()