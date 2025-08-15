# N.A.V.A - New Age Voice Assistant 🎙️🤖
NAVA (New Age Voice Assistant) is a Python-powered smart assistant designed to make your daily tasks easier using just your voice.
It can search the web, predict weather, answer questions, fetch Wikipedia summaries, read out news, and much more — all from your terminal. 
        ✨ Features

🎤 Voice Recognition – Understands your voice commands using speech_recognition.
🗣 Text-to-Speech – Replies back in natural voice with pyttsx3
🌐 Web Search – Fetches top results from Google
☁ Weather Updates – Uses OpenWeatherMap API to predict weather for any city. (Work in Progress) 
📰 Latest Programming News – Uses Web Scraping via BeautifulSoups to get the top news of the programming world. (Work in Progress)
📂 File Handeling - Capable of performing operations related to file handeling. (Work in Progress) 


🛠 How NAVA Works
NAVA’s Workflow:

Voice Input 🎤
The user speaks a command into the microphone.
speech_recognition converts the audio into text.

Command Analysis 🧠
The recognized text is checked against predefined keywords and actions.
If the command is a web search, NAVA initiates a Google search query.
If it’s a system command, NAVA uses subprocess to execute it.

Information Retrieval 🌐
NAVA sends the search query to Google Search and collects relevant results.
These results are passed to Gemini Flash API, which processes and refines the answer for clarity and accuracy.

Response Creation 📄
The Gemini API’s refined text is formatted for output.
For weather, news, or other APIs, NAVA fetches the result directly.

Voice Output 🔊
Using pyttsx3 (offline), the result is spoken back to the user.
subprocess can also be used to open web pages, applications, or files if required.
