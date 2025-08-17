import pyttsx3
import platform
from gtts import gTTS
import os


def _init_engine():
    system = platform.system()
    try:
        if system == "Windows":
            return pyttsx3.init("sapi5")
        elif system == "Darwin":  # macOS
            return pyttsx3.init("nsss")
        else:  # Linux
            return pyttsx3.init("espeak")
    except Exception as e:
        print(f"[WARN] pyttsx3 failed to initialize: {e}")
        return None


def text_to_speech(text):
    engine = _init_engine()
    if engine:
        engine.say(text)
        engine.runAndWait()
    else:
        # fallback: gTTS
        print("[INFO] Using gTTS fallback...")
        tts = gTTS(text=text, lang="en")
        tts.save("tts_output.mp3")
        if platform.system() == "Darwin":  
            os.system("afplay tts_output.mp3")
        elif platform.system() == "Windows":
            os.system("start tts_output.mp3")
        else:  # Linux
            os.system("mpg123 tts_output.mp3")


def text_to_speech_female(text):
    engine = _init_engine()
    if engine:
        voices = engine.getProperty("voices")
        for voice in voices:
            if "female" in voice.name.lower():
                engine.setProperty("voice", voice.id)
                break
        engine.say(text)
        engine.runAndWait()
    else:
        text_to_speech(text)
