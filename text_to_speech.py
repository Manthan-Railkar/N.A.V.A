import pyttsx3 as pt 

def text_to_speech(x):
     engine = pt.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice',voices[0].id)
     rate = engine.getProperty('rate')
     engine.setProperty('rate', 150)
     engine.say(x)
     engine.runAndWait()

def text_to_speech_female(x):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait() 