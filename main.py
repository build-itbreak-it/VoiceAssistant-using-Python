#packages needed (pip install)
import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS, lang
import playsound
import os
import random
from time import ctime

r = sr.Recognizer() #obj for text to voice 

def record_audio(ask = False): #To record audio from microphone
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            
        #error control
        except sr.UnknownValueError:
            alexis_speak('Sorry, I did not get that!')
        except sr.RequestError:
            alexis_speak('Sorry, My speech service is down')

        return voice_data

#text to audio file generation function
def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    #greet functions
    if 'who are you' in voice_data:
        alexis_speak('I am your personal voice assistant! You can call me with my name.')
    if 'what is your name' in voice_data:
        alexis_speak('My name is SECRET!')

    #get time and date , month, day using device os package
    if 'what is the time right now' in voice_data:
        alexis_speak(ctime())

    #google search in browser
    if 'search' in voice_data:
        search = record_audio('what do you want to google for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for' + search)

    #location
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)

    #instagram 
    if 'open insta' in voice_data:
        
        url = 'https://www.instagram.com/build.itbreak.it/'
        webbrowser.get().open(url)
        alexis_speak('Opening build it break it.. Follow and share for awesome projects!')
    
    #joke data here or u can use a Rapid_api to fetch random jokes 
    if 'crack a joke' in voice_data:
      
        joke = record_audio('Alright! How do you count cows? ')
        if(joke=='how'):
            alexis_speak('with a cowculator')
        
    
    if 'nonsense' in voice_data:
        alexis_speak('Sorry! Will upgrade with a better one')
    
    #exit terminal
    if 'exit' in voice_data:
        exit()

time.sleep(1)
alexis_speak('Hello there, How can I help you ?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    
