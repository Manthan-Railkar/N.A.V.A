<img width="312" height="312" alt="image" src="https://github.com/user-attachments/assets/55a78cee-19b4-4fcc-8c68-2798efae476b" />


# 🎙️ N.A.V.A - New Age Voice Assistant 🤖

**N.A.V.A (New Age Voice Assistant)** is a Python-powered smart assistant designed to simplify daily tasks using just your **voice**.  
It can **search the web**, **predict weather**, **fetch Wikipedia summaries**, **read news**, **handle files**, and much more — all from your terminal.

---

**WE ARE WORKING ON THE UI FOR THE PROJECT, PLEASE BE PATIENT>>>>(TILL THEN TRY RUNNING OUR CODE ON THE TERMINAL AND ENJOY :) )**
## ✨ Features

- 🎤 **Voice Recognition** – Understands commands using `speech_recognition`
- 🗣 **Text-to-Speech** – Natural voice responses with `pyttsx3`
- 🌐 **Web Search** – Fetches top results from Google
- ☁ **Weather Updates** – Predict weather using **OpenWeatherMap API**
- 📰 **Programming News** – Get latest tech updates via **BeautifulSoup Web Scraping** _(Work in Progress)_
- 📂 **File Handling** – Perform basic file operations _(Work in Progress)_
- 🤖 **AI-Powered Answers** – Uses **Gemini Flash API** to refine and enhance responses

---

## 🛠 How N.A.V.A Works

1. **Voice Input 🎤**

   - Speak a command into the microphone
   - `speech_recognition` converts speech → text

2. **Command Analysis 🧠**

   - Text is matched against predefined commands
   - Web queries → Google Search
   - System commands → `subprocess` execution

3. **Information Retrieval 🌐**

   - Google results + APIs (Weather, News, Wikipedia)
   - Refined answers via **Gemini Flash API**

4. **Response Creation 📄**

   - API results are structured for clarity
   - Supports multiple data sources

5. **Voice Output 🔊**
   - Results are spoken aloud via `pyttsx3`
   - Optionally open apps/files/webpages via `subprocess`

---

## 🛠️ Tech Stack

**Language:** Python 3.9+

**Core Libraries & APIs**

- `google-generativeai` → Gemini API integration
- `speech_recognition` → Convert speech → text
- `pyttsx3` → Offline text-to-speech
- `googlesearch-python` → Google search results
- `datetime` → Logging & timestamps
- `subprocess`, `platform`, `shutil` → System interaction
- Custom modules → `web_search`, `weather_predicter`, `text_to_speech`

---

## 🔑 API Keys Setup

N.A.V.A requires a **Gemini API key** (Google Generative AI).

### 👉 Steps to Get a Gemini API Key:

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **“Create API Key”**
4. Copy the key and store it securely

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/NAVA.git
   cd NAVA
   ```
2. **Install Dependencies**
   pip install -r requirements.txt
3. **ADD GEMINI API KEY**
   Add your api key in the Api_key variable

**WE RECOMMEND YOU TO CREATE A '.env' file**

## 🔑 Mode Switch Keywords

N.A.V.A. listens for specific **keywords** to decide what mode or task to execute.  
⚠️ Since this project is still in active development, **some keywords may not work yet or are partially functional.**

| 🗝️ Keyword       | 🚀 Mode / Action Triggered                                                    | Status         |
| ---------------- | ----------------------------------------------------------------------------- | -------------- |
| **"weather"**    | Switches to Weather Mode 🌦 – Fetches and reads out weather info for a city.   | ✅ Working     |
| **"web search"** | Switches to Web Search Mode 🔍 – Performs a Google search using Gemini API.   | ✅ Working     |
| **"news"**       | Switches to News Mode 📰 – Reads the latest programming/tech news.            | ⚠️ In Progress |
| **"file"**       | Switches to File Handling Mode 📂 – Supports file create/read/delete actions. | ⚠️ In Progress |
| **"time"**       | Switches to Time Mode ⏰ – Tells the current system time.                     | ⚠️ In Progress |
| **"date"**       | Switches to Date Mode 📅 – Tells today’s date.                                | ⚠️ In Progress |
| **"exit"**       | Ends the session and closes N.A.V.A ❌.                                       | ✅ Working     |

👉 Example commands after switching modes:

- `"weather in Mumbai"`
- `"search Python projects on GitHub"`
- `"file create notes.txt"`
