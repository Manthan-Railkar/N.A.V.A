from googlesearch import search
import subprocess
import platform
import shutil
import time
import os

def web_searcher(): 
  print("Write 'exit' to close the web search mode")
  while True: 
    query = input("What do you need? ")
    if(query.lower()=="exit"):
        
        break 
    urls = list(search(query, num_results=2))
    url = urls[1]

    device = platform.system().lower()

    if device == "windows":
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path, "--new-window", url])
        else:
            raise FileNotFoundError("Chrome not found at expected path on Windows.")

    elif device == "darwin":  # macOS
        chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path, "--new-window", url])
        else:
            raise FileNotFoundError("Chrome not found at expected path on macOS.")

    elif device == "linux":
        chrome_path = shutil.which("google-chrome") or shutil.which("chrome") or shutil.which("chromium-browser")
        if chrome_path:
            subprocess.Popen([chrome_path, "--new-window", url])
        else:
            raise FileNotFoundError("Chrome not found on Linux.")

    else:
        raise Exception("Unsupported Operating System.")

    time.sleep(3)  
