import pyttsx3 
import time

def text_to_speech(text):
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate','rate=150')
    time.sleep(0.4) 
    engine.say(text)
    engine.runAndWait()


