import google.generativeai as Genai 
import os
import speech_recognition as sr
from datetime import datetime
import text_to_speech
import pyttsx3 as pt 
from googlesearch import search
import subprocess
import platform
import shutil
import time
import os
import web_search
import weather_predicter

Api_key = "AIzaSyCZLyFUu730wnfg0oJ7AqEhOmxLwKYci8k"

#Gemini api setup 
def gemini_setup(Api_key):
  Genai.configure(api_key=Api_key) 
  model = Genai.GenerativeModel("gemini-2.0-flash") 
  return model  
  

def speech_to_text(): 
  file_name = input("Enter name of file txt : ")
  OUTPUT_FILE = f"{file_name}.txt"
  r = sr.Recognizer()

  print("Welcome to N.A.V.A, a Voice-controlled Gemini! Say 'start' to start the conversation. Say 'exit' to quit.")
  gemini_model = gemini_setup(Api_key)
  chat = gemini_model.start_chat()
  while True:
      with sr.Microphone() as source:
          print("\n🎤 Listening...")
          r.adjust_for_ambient_noise(source)  # optional for background noise
          audio = r.listen(source)

      try:
          # Convert speech to text
          user_input = r.recognize_google(audio)

          
          with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
              f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] You: {user_input}\n")

          if(user_input.lower()=="web search"):
              text_to_speech.text_to_speech("Changing to WEB SEARCH Mode")
              web_search.web_searcher()
              text_to_speech.text_to_speech("Changing Mode to Normal")
              continue

          elif(user_input.lower()=="gemini"):
              text_to_speech.text_to_speech("Changing to AI mode")
              while True:
                  with sr.Microphone() as source:
                      print("\n🎤 Listening...")
                      r.adjust_for_ambient_noise(source)  
                      audio = r.listen(source)
                  try: 
                      user_input = r.recognize_google(audio)

                      
                      with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                          f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] You: {user_input}\n")

                      print(f"You said: {user_input}")
                      response = chat.send_message(user_input) 
                      print(f'Gemini: {response.text}')
                      text_to_speech.text_to_speech_female(response.text)

                      
                      with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                          f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Gemini: {response.text}\n")

                  except sr.UnknownValueError:
                      print(" Could not understand audio")
                  except sr.RequestError as e:
                      print(f"Could not request results from Google Speech Recognition; {e}")
                  # Exit condition
                  if user_input.lower() == "exit":
                      text_to_speech.text_to_speech_female("Changing to Normal Mode")
                      break
          elif(user_input.lower()=="weather report"):
              text_to_speech.text_to_speech("Tell me the city to give the weather report")
              while True:
                  with sr.Microphone() as source:
                      print("\n🎤 Listening...")
                      r.adjust_for_ambient_noise(source)  
                      audio = r.listen(source) 
                  try:
                      user_input = r.recognize_google(audio)
                      if(user_input.lower()=="exit"):
                          text_to_speech.text_to_speech("Exiting...")
                          break
                      city,weather,unit = weather_predicter.get_data(user_input.lower())
                      text_to_speech.text_to_speech(f'City : {city} , Weather : {weather}, {unit}')
                  except sr.UnknownValueError:
                      print(" Could not understand audio")
                  except sr.RequestError as e:
                      print(f"Could not request results from Google Speech Recognition; {e}")

          print(f"You said: {user_input}")
          response = chat.send_message(user_input) 
          print(f'Nava: {response.text}')
          text_to_speech.text_to_speech(response.text)

          
          with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
              f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Nava: {response.text}\n")

          # Exit condition
          if user_input.lower() == "exit":
              print("Goodbye!")
              break

      except sr.UnknownValueError:
          print(" Could not understand audio")
      except sr.RequestError as e:
          print(
              f" Could not request results from Google Speech Recognition; {e}")

if __name__ == "__main__":
    speech_to_text()
