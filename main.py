import google.generativeai as Genai
import os
import speech_recognition as sr
from datetime import datetime
import text_to_speech
from googlesearch import search
import subprocess
import platform
import shutil
import time
import web_search
import weather_predicter

API_KEY = "gemini_api_key"


# Gemini API setup
def gemini_setup(api_key):
    Genai.configure(api_key=api_key)
    model = Genai.GenerativeModel("gemini-2.0-flash")
    return model


def speech_to_text():
    file_name = input("Enter a name for the file to save the conversation: ")
    OUTPUT_FILE = f"{file_name}.txt"
    r = sr.Recognizer()

    print("Welcome to N.A.V.A, a Voice-controlled Gemini!")
    print("Say 'web search' for search, 'gemini' for AI mode, 'weather' for forecast, 'exit' to quit.")

    gemini_model = gemini_setup(API_KEY)
    chat = gemini_model.start_chat()

    while True:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            user_input = r.recognize_google(audio)
            print(f"You said: {user_input}")

            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(
                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] You: {user_input}\n")

            # Exit the program
            if user_input.lower() == "exit":
                print("👋 Goodbye!")
                text_to_speech.text_to_speech("Goodbye! Have a nice day.")
                break

            # Web search mode
            elif user_input.lower() == "web search":
                text_to_speech.text_to_speech("Changing to WEB SEARCH mode")
                web_search.web_searcher()
                text_to_speech.text_to_speech("Returning to normal mode")
                continue

            # Gemini AI mode
            elif user_input.lower() == "gemini":
                text_to_speech.text_to_speech("Changing to AI mode")
                while True:
                    with sr.Microphone() as source:
                        print("\n🎤 Listening in Gemini Mode...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    try:
                        gemini_input = r.recognize_google(audio)
                        print(f"You said: {gemini_input}")

                        if gemini_input.lower() == "exit":
                            text_to_speech.text_to_speech("Exiting AI mode")
                            break

                        response = chat.send_message(gemini_input)
                        print(f'Gemini: {response.text}')
                        text_to_speech.text_to_speech_female(response.text)

                        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                            f.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Gemini: {response.text}\n")

                    except sr.UnknownValueError:
                        print(" Could not understand audio")
                    except sr.RequestError as e:
                        print(f" Google Speech Recognition error: {e}")

            # Weather mode
            elif user_input.lower() == "weather":
                text_to_speech.text_to_speech(
                    "Tell me the city to get the weather conditions")
                while True:
                    with sr.Microphone() as source:
                        print("\n🎤 Listening for city...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    try:
                        weather_input = r.recognize_google(audio)
                        print(f"You said: {weather_input}")

                        # Exit from weather mode
                        if weather_input.lower() == "exit":
                            text_to_speech.text_to_speech(
                                "Exiting weather mode")
                            break

                        weather = weather_predicter.get_data(weather_input)
                        print(f"NAVA: Weather - {weather}")
                        text_to_speech.text_to_speech(f"Weather: {weather}")

                    except sr.UnknownValueError:
                        print("Could not understand audio")
                    except sr.RequestError as e:
                        print(f"Google Speech Recognition error: {e}")

            # Normal mode (Gemini chat)
            else:
                response = chat.send_message(user_input)
                print(f"NAVA: {response.text}")
                text_to_speech.text_to_speech(response.text)

                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] NAVA: {response.text}\n")

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")


if __name__ == "__main__":
    speech_to_text()
